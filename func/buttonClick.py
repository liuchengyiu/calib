from PyQt5.QtWidgets import QMessageBox
from calib.lib.index import trans_to_16, createFrame, trans_floats_to_bytes, send_frame, batebcd_to_int, jcread_to_int
from calib.comSerial.run import seartCaLib
from calib.comSerial.triphase import triphase_run
from calib.comSerial.jc import jc_run
from calib.comSerial.run import jc_relative_power, send_tr_list

def startCaLib(self, mainWindow):
	frame = createFrame(105, 1, [], 67)
	send_frame(frame, mainWindow)

def sudoCaLib(self, mainWindow):
	seartCaLib(mainWindow)

def temperatureCalib(self, mainWindow):
	try:
		data = []
		data.append(mainWindow.tempSpinBox.value())
		data = trans_floats_to_bytes(data)	#温度校准
		frame = createFrame(105, 5, data, 67)
		send_frame(frame, mainWindow)
	except Exception as e:
		print(e)


def powerGainCompensation(self, mainWindow):
	try:
		value = mainWindow.powerGainCompensationParamDialog.getValue()
		data = [value['mask']]
		data.extend(trans_floats_to_bytes(value['phase_a']))
		data.extend(trans_floats_to_bytes(value['phase_b']))
		data.extend(trans_floats_to_bytes(value['phase_c']))
		frame = createFrame(105, 6, data, 67)
		send_frame(frame, mainWindow)
	except Exception as e:
		print(e)


def startPrice(self, mainWindow):
	data = []
	value = mainWindow.startPriceParamDialog.getValue()
	data.append(value['electricity'])
	data.append(value['power'])
	data = trans_floats_to_bytes(data)
	frame = createFrame(105, 4, data, 67)
	send_frame(frame, mainWindow)


def phaseCorrection(self, mainWindow):
	value = mainWindow.phaseCorrectionParamDialog.getValue()
	data = [value['mask']]
	data.extend(trans_floats_to_bytes(value['phase_a']))
	data.extend(trans_floats_to_bytes(value['phase_b']))
	data.extend(trans_floats_to_bytes(value['phase_c']))
	frame = createFrame(105, 7, data, 67)
	send_frame(frame, mainWindow)


def powerOffset(self, mainWindow):
	value = mainWindow.powerOffsetParamDialog.getValue()
	data = [value['mask']]
	data.extend(trans_floats_to_bytes(value['phase_a']))
	data.extend(trans_floats_to_bytes(value['phase_b']))
	data.extend(trans_floats_to_bytes(value['phase_c']))
	frame = createFrame(105, 8, data, 67)
	send_frame(frame, mainWindow)


def powerRms(self, mainWindow):
	frame = createFrame(105, 9, [], 67)
	send_frame(frame, mainWindow)


def voltageCurrentGain(self, mainWindow):
	value = mainWindow.voltageCurrentWeightParamDialog.getValue()
	data = [value['mask']]
	data.extend(trans_floats_to_bytes(value['phase_a']))
	data.extend(trans_floats_to_bytes(value['phase_b']))
	data.extend(trans_floats_to_bytes(value['phase_c']))
	frame = createFrame(105, 10, data, 67)
	send_frame(frame, mainWindow)

def stopCaLib(self, mainWindow):
	frame = createFrame(105, 11, [], 67)
	send_frame(frame, mainWindow)

def readData(self, mainWindow):

	frame = createFrame(105, 16, [], 67)
	send_frame(frame, mainWindow)
