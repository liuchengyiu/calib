import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtWidgets
from calib.component import HocCombobox, HocPushButton, My_WeightParamDialog, My_voltageCurrentWeightParamDialog, My_phaseCorrectionParamDialog, My_subsectionParamDialog, My_startPriceParamDialog
import sys
from calib.window import Ui_MainWindow
from calib.func import *
from calib.comSerial import Com
from time import sleep

class My_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(My_MainWindow, self).__init__()
        self.Com = Com(self, '')
        self.powerCom = Com(self, 'power')
        self.setupUi(self)
        self.tempSpinBox.setValue(25)
        # self.tempSpinBox.setReadOnly(True)
        self.powerGainCompensationParamDialog = My_WeightParamDialog()
        self.powerOffsetParamDialog = My_WeightParamDialog()
        self.voltageCurrentWeightParamDialog = My_voltageCurrentWeightParamDialog()
        self.phaseCorrectionParamDialog = My_phaseCorrectionParamDialog()
        self.subsectionParamDialog = My_subsectionParamDialog()
        self.startPriceParamDialog = My_startPriceParamDialog()
        self.calibComComboBox = HocCombobox(self.calibComComboBox, beforeMousePressEvent=listComName)
        self.calibBaudComboBox = HocCombobox(self.calibBaudComboBox, beforeMousePressEvent=listBaudRate)
        self.calibStopBitsComboBox = HocCombobox(self.calibStopBitsComboBox, beforeMousePressEvent=listStopBits)
        self.calibParityComboBox = HocCombobox(self.calibParityComboBox, beforeMousePressEvent=listParity)
        self.calibDataBitsComboBox = HocCombobox(self.calibDataBitsComboBox, beforeMousePressEvent=listDataBits)
        self.openComButton = HocPushButton(self.openComButton, beforeClick=openButton, MainWindow=self)
        self.calibComComboBox_power = HocCombobox(self.calibComComboBox_power, beforeMousePressEvent=listComName)
        self.calibBaudComboBox_power = HocCombobox(self.calibBaudComboBox_power, beforeMousePressEvent=listBaudRatePower)
        self.calibStopBitsComboBox_power = HocCombobox(self.calibStopBitsComboBox_power, beforeMousePressEvent=listStopBits)
        self.calibParityComboBox_power = HocCombobox(self.calibParityComboBox_power, beforeMousePressEvent=listParity)
        self.calibDataBitsComboBox_power = HocCombobox(self.calibDataBitsComboBox_power, beforeMousePressEvent=listDataBits)
        self.openComButton_power = HocPushButton(self.openComButton_power, beforeClick=openPowerButton, MainWindow=self)
        self.frameTextEdit.setReadOnly(True)
        self.powerGainCompensationParamPushButton = HocPushButton(
            self.powerGainCompensationParamPushButton, beforeClick=powerGainCompensationParamShow, MainWindow=self)
        self.powerOffsetParamPushButton = HocPushButton(
            self.powerOffsetParamPushButton, beforeClick=powerOffsetParamShow, MainWindow=self)
        self.voltageCurrentGainParamPushButton = HocPushButton(
            self.voltageCurrentGainParamPushButton, beforeClick=voltageCurrentGainParamShow, MainWindow=self)
        self.subsectionParamPushButton = HocPushButton(
            self.subsectionParamPushButton, beforeClick=subsectionParamShow, MainWindow=self)
        self.startPriceParamPushButton = HocPushButton(
            self.startPriceParamPushButton, beforeClick=startPriceParamShow, MainWindow=self)
        self.phaseCorrectionParamPushButton = HocPushButton(
            self.phaseCorrectionParamPushButton, beforeClick=phaseCorrectionParamShow, MainWindow=self)

        self.startPushButton = HocPushButton(
            self.startPushButton, beforeClick=startCaLib, MainWindow=self)
        self.autoPushButton = HocPushButton(
            self.autoPushButton, beforeClick=sudoCaLib, MainWindow=self)
        self.tempPushButton = HocPushButton(
            self.tempPushButton, beforeClick=temperatureCalib, MainWindow=self)
        self.powerGainCompensationPushButton = HocPushButton(
            self.powerGainCompensationPushButton, beforeClick=powerGainCompensation, MainWindow=self)

        self.phaseCorrectionPushButton = HocPushButton(
            self.phaseCorrectionPushButton, beforeClick=phaseCorrection, MainWindow=self)
        self.powerOffsetPushButton = HocPushButton(
            self.powerOffsetPushButton, beforeClick=powerOffset, MainWindow=self)
        self.powerRmsPushButton = HocPushButton(
            self.powerRmsPushButton, beforeClick=powerRms, MainWindow=self)
        self.voltageCurrentGainPushButton = HocPushButton(
            self.voltageCurrentGainPushButton, beforeClick=voltageCurrentGain, MainWindow=self)
        self.subsectionPushButton = HocPushButton(
            self.subsectionPushButton, beforeClick=subsection, MainWindow=self)
        self.startPricePushButton = HocPushButton(
            self.startPricePushButton, beforeClick=startPrice, MainWindow=self)
        self.readDataPushButton = HocPushButton(
            self.readDataPushButton, beforeClick=readData, MainWindow=self)
        self.stopPushButton = HocPushButton(
            self.stopPushButton, beforeClick=stopCaLib, MainWindow=self)

    def closeEvent(self, event) -> None:
        self.Com.Exit()
        sleep(1)
        event.accept()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myMain = My_MainWindow()
    myMain.show()
    app.exec_()
    sys.exit(0)


