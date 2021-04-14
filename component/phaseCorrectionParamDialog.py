from calib.window import Ui_phaseCorrectionParamDialog
from PyQt5 import QtWidgets


class My_phaseCorrectionParamDialog(QtWidgets.QDialog, Ui_phaseCorrectionParamDialog):
    def __init__(self):
        super(My_phaseCorrectionParamDialog, self).__init__()
        self.setupUi(self)
        self.okPushButton.clicked.connect(self.close)
        self.cancelPushButton.clicked.connect(self.close)

    def getValue(self) -> dict:
        phase = self.weightPhaseSpinBox.value()
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
        return {'phase': phase, 'mask': mask, 'phase_a': phase_a, 'phase_b': phase_b, 'phase_c': phase_c}
