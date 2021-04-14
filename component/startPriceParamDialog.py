from calib.window import Ui_startPriceParamDialog
from PyQt5 import QtWidgets


class My_startPriceParamDialog(QtWidgets.QDialog, Ui_startPriceParamDialog):
    def __init__(self):
        super(My_startPriceParamDialog, self).__init__()
        self.setupUi(self)
        self.okPushButton.clicked.connect(self.close)
        self.cancelPushButton.clicked.connect(self.close)

    def getValue(self) -> dict:
        electricity = self.startElectricityDoubleSpinBox.value()
        power = self.startPowerDoubleSpinBox.value()
        return {'electricity': electricity, 'power': power}
