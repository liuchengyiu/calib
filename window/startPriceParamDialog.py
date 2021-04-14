# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startPriceParamDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_startPriceParamDialog(object):
    def setupUi(self, startPriceParamDialog):
        startPriceParamDialog.setObjectName("startPriceParamDialog")
        startPriceParamDialog.resize(426, 212)
        self.startElectricityDoubleSpinBox = QtWidgets.QDoubleSpinBox(startPriceParamDialog)
        self.startElectricityDoubleSpinBox.setGeometry(QtCore.QRect(210, 70, 62, 22))
        self.startElectricityDoubleSpinBox.setDecimals(4)
        self.startElectricityDoubleSpinBox.setMaximum(999.0)
        self.startElectricityDoubleSpinBox.setObjectName("startElectricityDoubleSpinBox")
        self.label_3 = QtWidgets.QLabel(startPriceParamDialog)
        self.label_3.setGeometry(QtCore.QRect(150, 70, 54, 22))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(startPriceParamDialog)
        self.label_5.setGeometry(QtCore.QRect(150, 100, 54, 22))
        self.label_5.setObjectName("label_5")
        self.startPowerDoubleSpinBox = QtWidgets.QDoubleSpinBox(startPriceParamDialog)
        self.startPowerDoubleSpinBox.setGeometry(QtCore.QRect(210, 100, 62, 22))
        self.startPowerDoubleSpinBox.setDecimals(4)
        self.startPowerDoubleSpinBox.setMaximum(999.0)
        self.startPowerDoubleSpinBox.setObjectName("startPowerDoubleSpinBox")
        self.okPushButton = QtWidgets.QPushButton(startPriceParamDialog)
        self.okPushButton.setGeometry(QtCore.QRect(110, 170, 75, 23))
        self.okPushButton.setObjectName("okPushButton")
        self.cancelPushButton = QtWidgets.QPushButton(startPriceParamDialog)
        self.cancelPushButton.setGeometry(QtCore.QRect(240, 170, 75, 23))
        self.cancelPushButton.setObjectName("cancelPushButton")

        self.retranslateUi(startPriceParamDialog)
        QtCore.QMetaObject.connectSlotsByName(startPriceParamDialog)

    def retranslateUi(self, startPriceParamDialog):
        _translate = QtCore.QCoreApplication.translate
        startPriceParamDialog.setWindowTitle(_translate("startPriceParamDialog", "分量参数"))
        self.label_3.setText(_translate("startPriceParamDialog", "起动电流"))
        self.label_5.setText(_translate("startPriceParamDialog", "启动功率"))
        self.okPushButton.setText(_translate("startPriceParamDialog", "确定"))
        self.cancelPushButton.setText(_translate("startPriceParamDialog", "取消"))
