from calib.window import Ui_subsectionParamDialog
from PyQt5 import QtWidgets


class My_subsectionParamDialog(QtWidgets.QDialog, Ui_subsectionParamDialog):
    def __init__(self):
        super(My_subsectionParamDialog, self).__init__()
        self.setupUi(self)
        self.okPushButton.clicked.connect(self.close)
        self.cancelPushButton.clicked.connect(self.close)

    def getValue(self) -> dict:
        Iregion0 = self.Iregion0SubsectionDoubleSpinBox.value()
        Iregion1 = self.Iregion1SubsectionDoubleSpinBox.value()
        return {'Iregion0': Iregion0, 'Iregion1': Iregion1}
