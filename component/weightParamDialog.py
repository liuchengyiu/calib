from calib.window import Ui_weightParamDialog
from PyQt5 import QtWidgets


class My_WeightParamDialog(QtWidgets.QDialog, Ui_weightParamDialog):
    def __init__(self):
        super(My_WeightParamDialog, self).__init__()
        self.setupUi(self)
        self.okPushButton.clicked.connect(self.close)
        self.cancelPushButton.clicked.connect(self.close)

    def getValue(self) -> dict:
        mask = self.weightMaskSpinBox.value()
        phase_a = [
            self.phaseAVoltageDoubleSpinBox.value(),
            self.phaseACurrentDoubleSpinBox.value(),
            self.phaseAPowerFactorDoubleSpinBox.value()
        ]
        phase_b = [
            self.phaseBVoltageDoubleSpinBox.value(),
            self.phaseBCurrentDoubleSpinBox.value(),
            self.phaseBPowerFactorDoubleSpinBox.value()
        ]
        phase_c = [
            self.phaseCVoltageDoubleSpinBox.value(),
            self.phaseCCurrentDoubleSpinBox.value(),
            self.phaseCPowerFactorDoubleSpinBox.value()
        ]
        return {'mask': mask, 'phase_a': phase_a, 'phase_b': phase_b, 'phase_c': phase_c}
