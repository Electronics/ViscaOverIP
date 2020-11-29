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
	ZoomTeleVariable = lambda speed: byteSet(ZoomTele, (speed & 7) | 0x20, 4)
	ZoomWideVariable = lambda speed: byteSet(ZoomTele, (speed & 7) | 0x30, 4)
	ZoomPos = None #TODO: I don't understand this function
	DigitalZoomOn = bytearray.fromhex("8101040602ff")
	DigitalZoomOff = bytearray.fromhex("8101040603ff")
	FocusStop = bytearray.fromhex("8101040800ff")
	FocusFar = bytearray.fromhex("8101040802ff")
	FocusNear = bytearray.fromhex("8101040803ff")
	FocusFarVariable = lambda speed: byteSet(FocusFar, (speed & 7) | 0x20, 4)
	FocusNearVariable = lambda speed: byteSet(FocusFar, (speed & 7) | 0x30, 4)
	FocusPos = None #TODO: don't undersand this
	AutoFocus = bytearray.fromhex("8101043802ff")
	ManualFocus = bytearray.fromhex("8101043803ff")
	AutoManualFocus = bytearray.fromhex("8101043810ff") # switches?
	FocusOnePush = bytearray.fromhex("8101041801ff")
	FocusInfinity = bytearray.fromhex("8101041802ff")
	FocusNearLimit = None #TODO: don't understand this
	AutoFocusSensitivityNormal = bytearray.fromhex("8101045802ff")
	AutoFocusSensitivityLow = bytearray.fromhex("8101045803ff")
	AutoFocusModeNormal = bytearray.fromhex("8101045700ff")
	AutoFocusModeInterval = bytearray.fromhex("8101045701ff")
	AutoFocusModeZoomTrigger = bytearray.fromhex("8101045702ff")
	AutoFocusModeIntervalTime = None #TODO: not exactly sure on this
	IRCorrectionStandard = bytearray.fromhex("8101041100ff")
	IRCorrectionIRLight = bytearray.fromhex("8101041101ff")
	ZoomFocus = None #TODO: again, not sure
	WBAuto = bytearray.fromhex("8101043500ff")
	WBIndoor = bytearray.fromhex("8101043501ff")
	WBOutdoor = bytearray.fromhex("8101043502ff")
	WBOnePush = bytearray.fromhex("8101043503ff")
	WBATW = bytearray.fromhex("8101043504ff")
	WBManual = bytearray.fromhex("8101043505ff")
	WBOnePushTrigger = bytearray.fromhex("8101041005ff")
	RGainReset = bytearray.fromhex("8101040300ff")
	RGainUp = bytearray.fromhex("8101040302ff")
	RGainDown = bytearray.fromhex("8101040303ff")
	RGainDirect = None #TODO: hm
	BGainReset = bytearray.fromhex("8101040400ff")
	BGainUp = bytearray.fromhex("8101040402ff")
	BGainDown = bytearray.fromhex("8101040403ff")
	BGainDirect = None  # TODO: hm
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
	ShutterDirect = None #TODO: hm
	IrisReset = bytearray.fromhex("8101040b00ff")
	IrisUp = bytearray.fromhex("8101040b02ff")
	IrisDown = bytearray.fromhex("8101040b03ff")
	IrisDirect = None  # TODO: hm
	GainReset = bytearray.fromhex("8101040c00ff")
	GainUp = bytearray.fromhex("8101040c02ff")
	GainDown = bytearray.fromhex("8101040c03ff")
	GainDirect = None  # TODO:
	GainAELimit = lambda gain: byteSet(bytearray.fromhex("8101042c00ff"),(gain & 0x0f), 4) # gain 4-F
	BrightUp = bytearray.fromhex("8101040d02ff")
	BrightDown = bytearray.fromhex("8101040d03ff")
	BrightDirect = None #TODO:
	ExposureCompOn = bytearray.fromhex("8101043e02ff")
	ExposureCompOff = bytearray.fromhex("8101043e03ff")
	ExposureCompReset = bytearray.fromhex("8101040e00ff")
	ExposureCompUp = bytearray.fromhex("8101040e02ff")
	ExposureCompDown = bytearray.fromhex("8101040e03ff")
	ExposureCompDirect = None #TODO
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
	ApertureDirect = None #TODO
	HighResolutionOn = bytearray.fromhex("8101045202ff")
	HighResolutionOff = bytearray.fromhex("8101045203ff")
	NoiseReductionOff = bytearray.fromhex("8101045300ff")
	NoiseReduction = lambda level: byteSet(NoiseReductionOff, level & 0x07, 4)
	GammaStandard = bytearray.fromhex("8101045b00ff")
	Gamma = lambda level: byteSet(GammaStandard, level & 0x07, 4)
	HighSensitivityOn = bytearray.fromhex("8101045e02ff")
	HighSensitivityOff = bytearray.fromhex("8101045e03ff")
	PictureEffectOff = bytearray.fromhex("8101046300ff")
	PictureEffectNegative = bytearray.fromhex("8101046302ff")
	PictureEffectBW = bytearray.fromhex("8101046304ff")
	MemoryReset = lambda preset: byteSet(bytearray.fromhex("8101043f0000ff"), preset & 0x07, 5)
	MemorySet = lambda preset: byteSet(bytearray.fromhex("8101043f0100ff"), preset & 0x07, 5)
	MemoryRecall = lambda preset: byteSet(bytearray.fromhex("8101043f0200ff"), preset & 0x07, 5)
	IDWrite = None #TODO: lambda id: byteSet(bytearray.fromhex("8101042200000000ff"),)
	ChromaSurpress = lambda level: byteSet(bytearray.fromhex("8101045f00ff"),level & 0xff, 4)
	ColorGain = None #TODO
	ColorHue = None #TODO
	LowLatencyLow = bytearray.fromhex("81017e015a02ff")
	LowLatencyNormal = bytearray.fromhex("81017e015a03ff")
	MenuOff = bytearray.fromhex("8101060603ff")
	VideoFormatChange = None #TODO
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
			panSpeed, tiltSpeed, pan[3], pan[2], pan[1], pan[0],
			tilt[3], tilt[2], tilt[1], tilt[0]
		))
	def PanTiltRes(self, panPos=0, tiltPos=0, panSpeed=1, tiltSpeed=1):
		pan = "%0.4x"%(panPos&0xFFFF)
		tilt = "%0.4x"%(tiltPos&0xFFFF)
		return bytearray.fromhex("81010603%0.2x%0.2x0%s0%s0%s0%s0%s0%s0%s0%sff"%(
			panSpeed, tiltSpeed, pan[3], pan[2], pan[1], pan[0],
			tilt[3], tilt[2], tilt[1], tilt[0]
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
			pos, pan[3], pan[2], pan[1], pan[0],
			tilt[3], tilt[2], tilt[1], tilt[0]
		))
	def PanTiltLimitClear(self, pos, panPos=0, tiltPos=0):# pos=1 UpRight, pos=0 DownLeft
		pan = "%0.4x"%(panPos&0xFFFF)
		tilt = "%0.4x"%(tiltPos&0xFFFF)
		return bytearray.fromhex("8101060701%0.2x0%s0%s0%s0%s0%s0%s0%s0%sff"%(
			pos, pan[3], pan[2], pan[1], pan[0],
			tilt[3], tilt[2], tilt[1], tilt[0]
		))


