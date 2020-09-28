from calib.window import Ui_voltageCurrentWeightParamDialog
from PyQt5 import QtWidgets


class My_voltageCurrentWeightParamDialog(QtWidgets.QDialog, Ui_voltageCurrentWeightParamDialog):
    def __init__(self):
        super(My_voltageCurrentWeightParamDialog, self).__init__()
        self.setupUi(self)
        self.okPushButton.clicked.connect(self.close)
        self.cancelPushButton.clicked.connect(self.close)

    def getValue(self) -> dict:
        mask = self.weightMaskSpinBox.value()
        phase_a = [
            self.phaseAVoltageDoubleSpinBox.value(),
            self.phaseACurrentDoubleSpinBox.value(),
        ]
        phase_b = [
            self.phaseBVoltageDoubleSpinBox.value(),
            self.phaseBCurrentDoubleSpinBox.value(),
        ]
        phase_c = [
            self.phaseCVoltageDoubleSpinBox.value(),
            self.phaseCCurrentDoubleSpinBox.value(),
        ]
        return {'mask': mask, 'phase_a': phase_a, 'phase_b': phase_b, 'phase_c': phase_c}
