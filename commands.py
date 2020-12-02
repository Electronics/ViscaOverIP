def bytesOR(b1,b2):
	if len(b1) != len(b2):
		raise ValueError("Array lengths are different")
	for i, b in enumerate(b2):
		b1[i] |= b
	return b1
def bytesAND(b1,b2):
	if len(b1) != len(b2):
		raise ValueError("Array lengths are different")
	for i, b in enumerate(b2):
		b1[i] &= b
	return b1
def byteSet(by, value, position):
	by[position] = value
	return by

class Commands:
	PowerOn = bytearray.fromhex("8101040002ff")
	PowerOff = bytearray.fromhex("8101040003ff")
	ZoomStop = bytearray.fromhex("8101040700ff")
	ZoomTele = bytearray.fromhex("8101040702ff")
	ZoomWide = bytearray.fromhex("8101040703ff")
	def ZoomTeleVariable(self, speed):
			return byteSet(self.ZoomTele, (speed & 7) | 0x20, 4)
	def ZoomWideVariable(self, speed):
			return byteSet(self.ZoomTele, (speed & 7) | 0x30, 4)
	def ZoomPos(self, pos):
		# 0-0x4000 analog, 0x4000-0x7AC0 digital
		pos = "%0.4x" % (pos & 0xFFFF)
		return bytearray.fromhex("810104470%s0%s0%s0%sff"%(pos[0],pos[1],pos[2],pos[3]))
	DigitalZoomOn = bytearray.fromhex("8101040602ff")
	DigitalZoomOff = bytearray.fromhex("8101040603ff")
	FocusStop = bytearray.fromhex("8101040800ff")
	FocusFar = bytearray.fromhex("8101040802ff")
	FocusNear = bytearray.fromhex("8101040803ff")
	def FocusFarVariable(self, speed):
			return byteSet(self.FocusFar, (speed & 7) | 0x20, 4)
	def FocusNearVariable(self, speed):
			return byteSet(self.FocusFar, (speed & 7) | 0x30, 4)
	def FocusPos(self, pos):
		# 0-0x4000?
		pos = "%0.4x" % (pos & 0xFFFF)
		return bytearray.fromhex("810104480%s0%s0%s0%sff" % (pos[0], pos[1], pos[2], pos[3]))
	AutoFocus = bytearray.fromhex("8101043802ff")
	ManualFocus = bytearray.fromhex("8101043803ff")
	AutoManualFocus = bytearray.fromhex("8101043810ff") # switches?
	FocusOnePush = bytearray.fromhex("8101041801ff")
	FocusInfinity = bytearray.fromhex("8101041802ff")
	def FocusNearLimit(self, pos):
		# 0-0x4000?
		pos = "%0.4x" % (pos & 0xFFFF)
		return bytearray.fromhex("810104280%s0%s0%s0%sff" % (pos[0], pos[1], pos[2], pos[3]))
	AutoFocusSensitivityNormal = bytearray.fromhex("8101045802ff")
	AutoFocusSensitivityLow = bytearray.fromhex("8101045803ff")
	AutoFocusModeNormal = bytearray.fromhex("8101045700ff")
	AutoFocusModeInterval = bytearray.fromhex("8101045701ff")
	AutoFocusModeZoomTrigger = bytearray.fromhex("8101045702ff")
	def AutoFocusModeIntervalTime(self, time, speed=7):
		speed = "%0.2x" % (speed & 0xFF)
		time = "%0.2x" % (time & 0xFF)
		return bytearray.fromhex("810104270%s0%s0%s0%sff" % (speed[0], speed[1], time[0], time[1]))
	IRCorrectionStandard = bytearray.fromhex("8101041100ff")
	IRCorrectionIRLight = bytearray.fromhex("8101041101ff")
	def ZoomFocus(self, zoomPos, focusPos):
		zoomPos = "%0.4x" % (zoomPos & 0xFFFF)
		focusPos = "%0.4x" % (focusPos & 0xFFFF)
		return bytearray.fromhex("810104470%s0%s0%s0%s0%s0%s0%s0%sff" % (zoomPos[0], zoomPos[1], zoomPos[2], zoomPos[3], focusPos[0], focusPos[1], focusPos[2], focusPos[3]))
	WBAuto = bytearray.fromhex("8101043500ff")
	WBIndoor = bytearray.fromhex("8101043501ff")
	WBOutdoor = bytearray.fromhex("8101043502ff")
	WBOnePush = bytearray.fromhex("8101043503ff")
	WBATW = bytearray.fromhex("8101043504ff")
	WBManual = bytearray.fromhex("8101043505ff")
	WBOnePushTrigger = bytearray.fromhex("8101041005ff")
	RGainReset = bytearray.fromhex("8101040300ff") # red gain (Manual WB)
	RGainUp = bytearray.fromhex("8101040302ff")
	RGainDown = bytearray.fromhex("8101040303ff")
	def RGainDirect(self, gain):
		gain = "%0.2x" % (gain & 0xFF)
		return bytearray.fromhex("8101044300000%s0%sff" % (gain[0], gain[1]))
	BGainReset = bytearray.fromhex("8101040400ff") # blue gain  (Manual WB)
	BGainUp = bytearray.fromhex("8101040402ff")
	BGainDown = bytearray.fromhex("8101040403ff")
	def BGainDirect(self, gain):
		gain = "%0.2x" % (gain & 0xFF)
		return bytearray.fromhex("8101044400000%s0%sff" % (gain[0], gain[1]))
	ExposureAuto = bytearray.fromhex("8101043900ff")
	ExposureManual = bytearray.fromhex("8101043903ff")
	ExposureShutterPriority = bytearray.fromhex("810104390aff")
	ExposureIrisPriority = bytearray.fromhex("810104390bff")
	ExposureBright = bytearray.fromhex("810104390dff")
	SlowShutterAuto = bytearray.fromhex("8101045a02ff")
	SlowShuterManual = bytearray.fromhex("8101045a03ff")
	ShutterReset = bytearray.fromhex("8101040a00ff")
	ShutterUp = bytearray.fromhex("8101040a02ff")
	ShutterDown = bytearray.fromhex("8101040a03ff")
	def ShutterDirect(self, pos):
		pos = "%0.2x" % (pos & 0xFF)
		return bytearray.fromhex("8101044a00000%s0%sff" % (pos[0], pos[1]))
	IrisReset = bytearray.fromhex("8101040b00ff")
	IrisUp = bytearray.fromhex("8101040b02ff")
	IrisDown = bytearray.fromhex("8101040b03ff")
	def IrisDirect(self, pos):
		pos = "%0.2x" % (pos & 0xFF)
		return bytearray.fromhex("8101044b00000%s0%sff" % (pos[0], pos[1]))
	GainReset = bytearray.fromhex("8101040c00ff")
	GainUp = bytearray.fromhex("8101040c02ff")
	GainDown = bytearray.fromhex("8101040c03ff")
	def GainDirect(self, pos):
		pos = "%0.2x" % (pos & 0xFF)
		return bytearray.fromhex("8101044c00000%s0%sff" % (pos[0], pos[1]))
	def GainAELimit(self, gain):
			return byteSet(bytearray.fromhex("8101042c00ff"),(gain & 0x0f), 4) # gain 4-F
	BrightUp = bytearray.fromhex("8101040d02ff")
	BrightDown = bytearray.fromhex("8101040d03ff")
	def BrightDirect(self, pos):
		pos = "%0.2x" % (pos & 0xFF)
		return bytearray.fromhex("8101044d00000%s0%s" % (pos[0], pos[1]))
	ExposureCompOn = bytearray.fromhex("8101043e02ff")
	ExposureCompOff = bytearray.fromhex("8101043e03ff")
	ExposureCompReset = bytearray.fromhex("8101040e00ff")
	ExposureCompUp = bytearray.fromhex("8101040e02ff")
	ExposureCompDown = bytearray.fromhex("8101040e03ff")
	def ExposureCompDirect(self, pos):
		pos = "%0.2x" % (pos & 0xFF)
		return bytearray.fromhex("8101044e00000%s0%sff" % (pos[0], pos[1]))
	BacklightCompOn = bytearray.fromhex("8101043302ff")
	BacklightCompOff = bytearray.fromhex("8101043303ff")
	WideDynamicRangeOff = bytearray.fromhex("81017e040000ff")
	WideDynamicRangeLow = bytearray.fromhex("81017e040001ff")
	WideDynamicRangeMed = bytearray.fromhex("81017e040002ff")
	WideDynamicRangeHigh = bytearray.fromhex("81017e040003ff")
	DefogOn = bytearray.fromhex("810104370200ff")
	DefogOff = bytearray.fromhex("810104370300ff")
	ApertureReset = bytearray.fromhex("8101040200ff")
	ApertureUp = bytearray.fromhex("8101040202ff")
	ApertureDown = bytearray.fromhex("8101040203ff")
	def ApertureDirect(self, gain):
		gain = "%0.2x" % (gain & 0xFF)
		return bytearray.fromhex("8101044200000%s0%s" % (gain[0], gain[1]))
	HighResolutionOn = bytearray.fromhex("8101045202ff")
	HighResolutionOff = bytearray.fromhex("8101045203ff")
	NoiseReductionOff = bytearray.fromhex("8101045300ff")
	def NoiseReduction(self, level):
		return byteSet(self.NoiseReductionOff, level & 0x07, 4)
	GammaStandard = bytearray.fromhex("8101045b00ff")
	def Gamma(self, level):
		return byteSet(self.GammaStandard, level & 0x07, 4)
	HighSensitivityOn = bytearray.fromhex("8101045e02ff")
	HighSensitivityOff = bytearray.fromhex("8101045e03ff")
	PictureEffectOff = bytearray.fromhex("8101046300ff")
	PictureEffectNegative = bytearray.fromhex("8101046302ff")
	PictureEffectBW = bytearray.fromhex("8101046304ff")
	MemoryReset = lambda preset: byteSet(bytearray.fromhex("8101043f0000ff"), preset & 0x07, 5)
	MemorySet = lambda preset: byteSet(bytearray.fromhex("8101043f0100ff"), preset & 0x07, 5)
	MemoryRecall = lambda preset: byteSet(bytearray.fromhex("8101043f0200ff"), preset & 0x07, 5)
	def IDWrite(self, id):
		id = "%0.4x" % (id & 0xFFFF)
		return bytearray.fromhex("810104220%s0%s0%s0%sff" % (id[0], id[1], id[2], id[3]))
	ChromaSurpress = lambda level: byteSet(bytearray.fromhex("8101045f00ff"),level & 0xff, 4)
	def ColorGain(self, spec, gain):
		return bytearray.fromhex("810104490000%0.2x%0.2xff" % (spec & 0x07, gain & 0x0f))
	def ColorHue(self, spec, phase):
		return bytearray.fromhex("8101044f0000%0.2x%0.2xff" % (spec & 0x07, phase & 0x0f))
	LowLatencyLow = bytearray.fromhex("81017e015a02ff")
	LowLatencyNormal = bytearray.fromhex("81017e015a03ff")
	MenuOff = bytearray.fromhex("8101060603ff")
	def VideoFormatChange(self, format):
		format = "%0.2x" % (format & 0xFF)
		return bytearray.fromhex("81017e011e0%s0%sff" % (format[0], format[1]))
	ColorSystem = lambda a: byteSet(bytearray.fromhex("81017e01030000ff"),a & 0x03, 6)
	IROn = bytearray.fromhex("8101060802ff")
	IROff = bytearray.fromhex("8101060803ff")
	IRToggle = bytearray.fromhex("8101060810ff")
	ReceiveReturnOn = bytearray.fromhex("81017d01030000ff")
	ReceiveReturnOff = bytearray.fromhex("81017d01130000ff")
	InfoDisplayOn = bytearray.fromhex("81017e011802ff")
	InfoDisplayOff = bytearray.fromhex("81017e011803ff")
	def PanTiltAbs(self, panPos=0, tiltPos=0, panSpeed=1, tiltSpeed=1):
		pan = "%0.4x"%(panPos&0xFFFF)
		tilt = "%0.4x"%(tiltPos&0xFFFF)
		return bytearray.fromhex("81010602%0.2x%0.2x0%s0%s0%s0%s0%s0%s0%s0%sff"%(
			panSpeed, tiltSpeed, pan[0], pan[1], pan[2], pan[3],
			tilt[0], tilt[1], tilt[2], tilt[3]
		))
	def PanTiltRel(self, panPos=0, tiltPos=0, panSpeed=1, tiltSpeed=1):
		pan = "%0.4x"%(panPos&0xFFFF)
		tilt = "%0.4x"%(tiltPos&0xFFFF)
		return bytearray.fromhex("81010603%0.2x%0.2x0%s0%s0%s0%s0%s0%s0%s0%sff"%(
			panSpeed, tiltSpeed, pan[0], pan[1], pan[2], pan[3],
			tilt[0], tilt[1], tilt[2], tilt[3]
		))
	def PanTiltUp(self, panSpeed=1, tiltSpeed=1):
		return bytearray.fromhex("81010601%0.2x%0.2x0301ff"%(panSpeed, tiltSpeed))
	def PanTiltDown(self, panSpeed=1, tiltSpeed=1):
		return bytearray.fromhex("81010601%0.2x%0.2x0302ff" % (panSpeed, tiltSpeed))
	def PanTiltLeft(self, panSpeed=1, tiltSpeed=1):
		return bytearray.fromhex("81010601%0.2x%0.2x0103ff" % (panSpeed, tiltSpeed))
	def PanTiltRight(self, panSpeed=1, tiltSpeed=1):
		return bytearray.fromhex("81010601%0.2x%0.2x0203ff" % (panSpeed, tiltSpeed))
	def PanTiltUpLeft(self, panSpeed=1, tiltSpeed=1):
		return bytearray.fromhex("81010601%0.2x%0.2x0101ff" % (panSpeed, tiltSpeed))
	def PanTiltUpRight(self, panSpeed=1, tiltSpeed=1):
		return bytearray.fromhex("81010601%0.2x%0.2x0201ff" % (panSpeed, tiltSpeed))
	def PanTiltDownLeft(self, panSpeed=1, tiltSpeed=1):
		return bytearray.fromhex("81010601%0.2x%0.2x0102ff" % (panSpeed, tiltSpeed))
	def PanTiltDownRight(self, panSpeed=1, tiltSpeed=1):
		return bytearray.fromhex("81010601%0.2x%0.2x0202ff" % (panSpeed, tiltSpeed))
	def PanTiltStop(self, panSpeed=1, tiltSpeed=1):
		return bytearray.fromhex("81010601%0.2x%0.2x0203ff" % (panSpeed, tiltSpeed))
	PanTiltHome = bytearray.fromhex("81010604ff")
	PanTiltReset = bytearray.fromhex("81010605ff")
	def PanTiltLimitSet(self, pos, panPos=0, tiltPos=0):# pos=1 UpRight, pos=0 DownLeft
		pan = "%0.4x"%(panPos&0xFFFF)
		tilt = "%0.4x"%(tiltPos&0xFFFF)
		return bytearray.fromhex("8101060700%0.2x0%s0%s0%s0%s0%s0%s0%s0%sff"%(
			pos, pan[0], pan[1], pan[2], pan[3],
			tilt[0], tilt[1], tilt[2], tilt[3]
		))
	def PanTiltLimitClear(self, pos, panPos=0, tiltPos=0):# pos=1 UpRight, pos=0 DownLeft
		pan = "%0.4x"%(panPos&0xFFFF)
		tilt = "%0.4x"%(tiltPos&0xFFFF)
		return bytearray.fromhex("8101060701%0.2x0%s0%s0%s0%s0%s0%s0%s0%sff"%(
			pos, pan[0], pan[1], pan[2], pan[3],
			tilt[0], tilt[1], tilt[2], tilt[3]
		))
Commands = Commands()

class Inquiry:
	Power = bytearray.fromhex("81090400ff")
	ZoomPos = bytearray.fromhex("81090447ff")
	DZoomMode = bytearray.fromhex("81090447ff")
	FocusMode = bytearray.fromhex("81090438ff")
	FocusPos = bytearray.fromhex("81090448ff")
	FocusNearLimit = bytearray.fromhex("81090428ff")
	AutoFocusSensitivty = bytearray.fromhex("81090458ff")
	AutoFocusMode = bytearray.fromhex("81090457ff")
	AutoFocusInterval = bytearray.fromhex("81090427ff")
	IR = bytearray.fromhex("81090411ff")
	WBMode = bytearray.fromhex("81090435ff")
	RGain = bytearray.fromhex("81090443ff")
	BGain = bytearray.fromhex("81090444ff")
	AEMode = bytearray.fromhex("81090439ff")
	SlowShutterMode = bytearray.fromhex("8109045aff")
	ShutterPos = bytearray.fromhex("8109044aff")
	IrisPos = bytearray.fromhex("8109044bff")
	GainPos = bytearray.fromhex("8109044cff")
	GainLimit = bytearray.fromhex("8109042cff")
	BrightPos = bytearray.fromhex("8109044dff")
	ExposureCompMode = bytearray.fromhex("8109043eff")
	ExposureCompPos = bytearray.fromhex("8109044eff")
	BacklightMode = bytearray.fromhex("81090433ff")
	WDMode = bytearray.fromhex("81097e0400ff")
	Defog = bytearray.fromhex("81090437ff")
	Aperture = bytearray.fromhex("81090442ff")
	HighResolutionMode = bytearray.fromhex("81090452ff")
	NR = bytearray.fromhex("81090453ff")
	Gamma = bytearray.fromhex("8109045bff")
	HighSensitivity = bytearray.fromhex("8109045eff")
	PictureEffectMode = bytearray.fromhex("81090463ff")
	ID = bytearray.fromhex("81090422ff")
	Version = bytearray.fromhex("81090002ff")
	ChromaSuppress = bytearray.fromhex("8109045fff")
	ColorGain = bytearray.fromhex("81090449ff")
	ColorHue = bytearray.fromhex("8109044fff")
	LowLatency = bytearray.fromhex("81097e015aff")
	MenuMode = bytearray.fromhex("81090606ff")
	InformationDisplay = bytearray.fromhex("81097e0118ff")
	VideoFormat = bytearray.fromhex("81090623ff")
	ColorSystem = bytearray.fromhex("81097e0103ff")
	IRReceive = bytearray.fromhex("81090608ff")
	IRCondition = bytearray.fromhex("81090634ff")
	PanTiltMaxSpeed = bytearray.fromhex("81090611ff")
	PanTiltPos = bytearray.fromhex("81090612ff")
	PanTiltMode = bytearray.fromhex("81090610ff")

	BlockLens = bytearray.fromhex("81097e7e00ff")
	BlockControl = bytearray.fromhex("81097e7e01ff")
	BlockOther = bytearray.fromhex("81097e7e02ff")
	BlockEnlargement = bytearray.fromhex("81097e7e03ff")
	BlockEnlargement2 = bytearray.fromhex("81097e7e04ff")
	BlockEnlargement3 = bytearray.fromhex("81097e7e05ff")

VideoFormats = {
	"1080p59": 0,
	"1080p29": 1,
	"1080i59": 2,
	"720p59": 3,
	"720p29": 4,
	"1080p50": 8,
	"1080p25": 0xA,
	"1080i50": 0xB,
	"720p50": 0xC,
	"720p25": 0xD
}
ColorSystems = {
	"HDMI-YUV": 0,
	"HDMI-GBR": 1,
	"DVI-GBR": 2,
	"DVI-YUV": 3
}
Iris = {
	"F1.8": 0x11,
	"F2.0": 0x10,
	"F2.4": 0xf,
	"F2.8": 0xe,
	"F3.4": 0xd,
	"F4": 0xc,
	"F4.8": 0xb,
	"F5.6": 0xa,
	"F6.8": 9,
	"F8": 8,
	"F9.6": 7,
	"F11": 6,
	"F14": 5,
	"CLOSE": 0
}