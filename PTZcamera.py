import socket
import logging as log
from commands import *
log.basicConfig(format='%(asctime)s %(message)s')
log.addLevelName(5,"VERBOSE")
log.getLogger().setLevel("VERBOSE")

socket.setdefaulttimeout(1)

class Camera:
	sequenceNumber = 1 # starts at 1?
	def __init__(self, name, ip, mac, netmask="255.255.255.0", gateway="0.0.0.0"):
		self.name = name
		self.ip = ip
		self.mac = mac # mac using dashes to seperate
		self.netmask = netmask
		self.gateway = gateway
		self.resetSequenceNumber()
	def __str__(self):
		return f"{self.name}({self.mac}) {self.ip}"

	def setIP(self, ip=None, netmask=None, gateway=None, name=None):
		# name must be up to 8 alphanumeric characters (and blank)
		if not ip:
			ip = self.ip
		if not netmask:
			netmask = self.netmask
		if not gateway:
			gateway = self.gateway
		if not name:
			name = self.name
		command = (b"\x02MAC:"+bytes(self.mac, encoding="utf-8")+b"\xFFIPADR:"+bytes(ip, encoding="utf-8")+
					b"\xFFMASK:"+bytes(netmask, encoding="utf-8")+b"\xFFGATEWAY:"+bytes(gateway, encoding="utf-8")+
					b"\xFFNAME:"+bytes(name, encoding="utf-8")+b"\xFF\x03")
		#sock.sendto(command, (self.ip, 52380))
		sendRawCommand(self.ip, command, port=52380)

	def sendCommand(self, command, skipCompletion=False):
		# for general commands (payload type 0100), command should be bytes
		length = len(command).to_bytes(2, 'big')
		command = b"\x01\x00" + length + self.sequenceNumber.to_bytes(4, 'big') + command
		data = sendRawCommand(self.ip, command, skipCompletion=skipCompletion) # TODO: deal with udp packets getting lost and sequence number desyncing (see manual)
		self.sequenceNumber += 1
		return data

	def inquire(self, command):
		return self.sendCommand(command, skipCompletion=True) # no acknoledge message for a inquiry

	def resetSequenceNumber(self):
		self.sequenceNumber = 1
		sendRawCommand(self.ip, bytearray.fromhex('02 00 00 01 00 00 00 01 01'), skipCompletion=True)

	def getPos(self):
		data = self.inquire(Inquiry.PanTiltPos)
		pan = (data[10] << 12) | (data[11] << 8) | (data[12] << 4) | data[13]
		tilt = (data[14] << 12) | (data[15] << 8) | (data[16] << 4) | data[17]
		log.debug("Got positions, Pan: %0.4x Tilt: %0.4x", pan, tilt)
		return (pan, tilt)


def sendRawCommand(ip, command, port=52381, skipCompletion=False):
	# this sends a command and waits for a response, note it does NOT calculate / use the sequence number
	# command should be a bytes object
	log.debug("Sending to %s: %r", ip, command)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(("", port))
	s.sendto(command, (ip, port))

	def receive():
		data = s.recv(1024)
		log.log(5, "Received %r", data)
		if b"NAK" in data:
			log.error("Command failed with error: %r", data)
		if len(data) > 10:
			if data[8] == 0x90:
				# acknowledged / completion / error message
				if data[9] == 0x41:
					log.debug("Command acknowledged successfully")
				if data[9] == 0x51:
					log.debug("Command completed successfully")
				if (data[9] & 0xf0) == 0x60:
					log.error("Command failed with error: %r", data)
					error = {0x01: "Message length error", 0x02: "Syntax Error", 0x03: "Command buffer full", 0x04: "Command canceled", 0x05: "No socket", 0x41: "Command not executable"}
					log.error("Formatted: %s",error.get(data[10], "Unknown"))
		else:
			if data == b'\x02\x01\x00\x01\x00\x00\x00\x00\x01':
				log.debug("Successfully reset sequence number")
			else:
				log.error("Returned data was too short?")
		return data

	try:
		data = receive() # acknolwedge
		if skipCompletion:
			return data
		data = receive() # completion
		return data
	except socket.timeout:
		log.error("Sendrawcommand timeout to %s", ip)
		return None
	finally:
		s.close()

def discoverCameras():
	# UDP socket, enable broadcast, and socket reuse (hah if even that worked)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	s.settimeout(1)

	try:
		s.bind(("", 52380))

		discoverCmd = b"\x02ENQ:network\xFF\x33"
		log.debug("Sending discover...")
		s.sendto(discoverCmd, ('<broadcast>', 52380))
		cameras = []
		try:
			while True:
				raw, addr = s.recvfrom(1024)
				if raw == discoverCmd:
					continue
				data = raw.split(b'\xFF')
				name = data[7][5:].decode("utf-8")
				mac = data[0][5:].decode("utf-8")
				log.info("Found camera %s (%s) at IP %s", name, mac, addr[0])
				cameras.append(Camera(name, addr[0], mac))
		except socket.timeout:
			log.debug("End discover")
		if len(cameras) == 0:
			return None
		return cameras
	finally:
		s.close()

c = discoverCameras()
d = Camera("CAM1", "10.0.1.90", "")
import time
# while True:
# 	d.sendCommand(b"\x81\x01\x06\x01\x18\x14\x02\x02\xFF") # move down
# 	time.sleep(1)
# 	d.sendCommand(b"\x81\x01\x06\x01\x18\x14\x01\x01\xFF") # move up
# 	time.sleep(1)

#d.sendCommand(b"\x81\x01\x7e\x01\x18\x02\xff")
#c[0].setIP(name="LaurieC1")
#c[0].sendCommand(b"\x81\x01\x7e\x01\x5a\x02\xff") # lowest latency
#d.sendCommand(Commands.PanTiltUp())
d.getPos()
