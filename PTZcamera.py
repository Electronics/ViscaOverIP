import socket
import logging as log
log.basicConfig(format='%(asctime)s %(message)s')
log.addLevelName(5,"VERBOSE")
log.getLogger().setLevel("VERBOSE")

socket.setdefaulttimeout(1)

class Camera:
	def __init__(self, name, ip, mac, netmask="255.255.255.0", gateway="0.0.0.0"):
		self.name = name
		self.ip = ip
		self.mac = mac # mac using dashes to seperate
		self.netmask = netmask
		self.gateway = gateway
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
		sendCommand(self.ip, command)

def sendCommand(ip, command):
	# this sends a command and waits for a response
	# command should be a bytes object
	log.debug("Sending to %s: %r", ip, command)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
	s.connect((ip, 52380))
	s.send(command)
	try:
		data = s.recv(1024)
		log.debug("Received %r",data)
		if b"NAK" in data:
			log.error("Command failed with error: %r", data)
		return data
	except socket.timeout:
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
#c[0].setIP(name="BOOBIES")
