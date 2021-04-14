# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subsectionParamDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subsectionParamDialog(object):
    def setupUi(self, subsectionParamDialog):
        subsectionParamDialog.setObjectName("subsectionParamDialog")
        subsectionParamDialog.resize(426, 212)
        self.Iregion0SubsectionDoubleSpinBox = QtWidgets.QDoubleSpinBox(subsectionParamDialog)
        self.Iregion0SubsectionDoubleSpinBox.setGeometry(QtCore.QRect(210, 70, 62, 22))
        self.Iregion0SubsectionDoubleSpinBox.setDecimals(4)
        self.Iregion0SubsectionDoubleSpinBox.setMaximum(999.0)
        self.Iregion0SubsectionDoubleSpinBox.setObjectName("Iregion0SubsectionDoubleSpinBox")
        self.label_3 = QtWidgets.QLabel(subsectionParamDialog)
        self.label_3.setGeometry(QtCore.QRect(150, 70, 54, 22))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(subsectionParamDialog)
        self.label_5.setGeometry(QtCore.QRect(150, 100, 54, 22))
        self.label_5.setObjectName("label_5")
        self.Iregion1SubsectionDoubleSpinBox = QtWidgets.QDoubleSpinBox(subsectionParamDialog)
        self.Iregion1SubsectionDoubleSpinBox.setGeometry(QtCore.QRect(210, 100, 62, 22))
        self.Iregion1SubsectionDoubleSpinBox.setDecimals(4)
        self.Iregion1SubsectionDoubleSpinBox.setMaximum(999.0)
        self.Iregion1SubsectionDoubleSpinBox.setObjectName("Iregion1SubsectionDoubleSpinBox")
        self.okPushButton = QtWidgets.QPushButton(subsectionParamDialog)
        self.okPushButton.setGeometry(QtCore.QRect(110, 170, 75, 23))
        self.okPushButton.setObjectName("okPushButton")
        self.cancelPushButton = QtWidgets.QPushButton(subsectionParamDialog)
        self.cancelPushButton.setGeometry(QtCore.QRect(240, 170, 75, 23))
        self.cancelPushButton.setObjectName("cancelPushButton")

        self.retranslateUi(subsectionParamDialog)
        QtCore.QMetaObject.connectSlotsByName(subsectionParamDialog)

    def retranslateUi(self, subsectionParamDialog):
        _translate = QtCore.QCoreApplication.translate
        subsectionParamDialog.setWindowTitle(_translate("subsectionParamDialog", "分量参数"))
        self.label_3.setText(_translate("subsectionParamDialog", "Iregion0"))
        self.label_5.setText(_translate("subsectionParamDialog", "Iregion1"))
        self.okPushButton.setText(_translate("subsectionParamDialog", "确定"))
        self.cancelPushButton.setText(_translate("subsectionParamDialog", "取消"))
