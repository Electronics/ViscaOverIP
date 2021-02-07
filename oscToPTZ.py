### Just a quick lash-together for OSC -> PTZ commands so I can use my streamdeck :)

from pythonosc import dispatcher
from pythonosc import osc_server

from PTZcamera import *

c = Camera("CAM1", "10.0.1.90", "")

def cameraHandler(address, *args):
	panSpeed = 0x08
	tiltSpeed = 0x08
	data = address.split("/")
	if data[2]=="up":
		c.sendCommand(Commands.PanTiltUp(panSpeed,tiltSpeed))
	elif data[2]=="down":
		c.sendCommand(Commands.PanTiltDown(panSpeed,tiltSpeed))
	elif data[2] == "left":
		c.sendCommand(Commands.PanTiltLeft(panSpeed,tiltSpeed))
	elif data[2] == "right":
		c.sendCommand(Commands.PanTiltRight(panSpeed,tiltSpeed))
	elif data[2] == "upleft":
		c.sendCommand(Commands.PanTiltUpLeft(panSpeed,tiltSpeed))
	elif data[2] == "upright":
		c.sendCommand(Commands.PanTiltUpRight(panSpeed,tiltSpeed))
	elif data[2] == "downleft":
		c.sendCommand(Commands.PanTiltDownLeft(panSpeed,tiltSpeed))
	elif data[2] == "downright":
		c.sendCommand(Commands.PanTiltDownRight(panSpeed,tiltSpeed))
	elif data[2] == "stop":
		c.sendCommand(Commands.PanTiltStop(panSpeed,tiltSpeed))
	elif data[2] == "zoomin":
		c.sendCommand(Commands.ZoomTele)
	elif data[2] == "zoomout":
		c.sendCommand(Commands.ZoomWide)
	elif data[2] == "zoomstop":
		c.sendCommand(Commands.ZoomStop)
	elif data[2] == "recall":
		try:
			mem = int(data[3])
			if mem < 8:
				c.sendCommand(Commands.MemoryRecall(mem))
		except:
			print("NYA")
			pass
	elif data[2] == "store":
		try:
			mem = int(data[3])
			if mem < 8:
				c.sendCommand(Commands.MemorySet(mem))
		except:
			print("NYA")
			pass

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/camera/*", cameraHandler)

server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 54000), dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()
