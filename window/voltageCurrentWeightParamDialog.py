# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voltageCurrentWeightParamDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# import sys, os
# if hasattr(sys, 'frozen'):
#     os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_voltageCurrentWeightParamDialog(object):
    def setupUi(self, voltageCurrentWeightParamDialog):
        voltageCurrentWeightParamDialog.setObjectName("voltageCurrentWeightParamDialog")
        voltageCurrentWeightParamDialog.resize(273, 185)
        self.label = QtWidgets.QLabel(voltageCurrentWeightParamDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 22))
        self.label.setObjectName("label")
        self.weightMaskSpinBox = QtWidgets.QSpinBox(voltageCurrentWeightParamDialog)
        self.weightMaskSpinBox.setGeometry(QtCore.QRect(70, 20, 61, 22))
        self.weightMaskSpinBox.setMaximum(999)
        self.weightMaskSpinBox.setObjectName("weightMaskSpinBox")
        self.label_2 = QtWidgets.QLabel(voltageCurrentWeightParamDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 54, 22))
        self.label_2.setObjectName("label_2")
        self.phaseAVoltageDoubleSpinBox = QtWidgets.QDoubleSpinBox(voltageCurrentWeightParamDialog)
        self.phaseAVoltageDoubleSpinBox.setGeometry(QtCore.QRect(70, 50, 62, 22))
        self.phaseAVoltageDoubleSpinBox.setMaximum(999.0)
        self.phaseAVoltageDoubleSpinBox.setObjectName("phaseAVoltageDoubleSpinBox")
        self.phaseACurrentDoubleSpinBox = QtWidgets.QDoubleSpinBox(voltageCurrentWeightParamDialog)
        self.phaseACurrentDoubleSpinBox.setGeometry(QtCore.QRect(200, 50, 62, 22))
        self.phaseACurrentDoubleSpinBox.setMaximum(999.0)
        self.phaseACurrentDoubleSpinBox.setObjectName("phaseACurrentDoubleSpinBox")
        self.label_3 = QtWidgets.QLabel(voltageCurrentWeightParamDialog)
        self.label_3.setGeometry(QtCore.QRect(140, 50, 54, 22))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(voltageCurrentWeightParamDialog)
        self.label_5.setGeometry(QtCore.QRect(140, 80, 54, 22))
        self.label_5.setObjectName("label_5")
        self.phaseBVoltageDoubleSpinBox = QtWidgets.QDoubleSpinBox(voltageCurrentWeightParamDialog)
        self.phaseBVoltageDoubleSpinBox.setGeometry(QtCore.QRect(70, 80, 62, 22))
        self.phaseBVoltageDoubleSpinBox.setMaximum(999.0)
        self.phaseBVoltageDoubleSpinBox.setObjectName("phaseBVoltageDoubleSpinBox")
        self.phaseBCurrentDoubleSpinBox = QtWidgets.QDoubleSpinBox(voltageCurrentWeightParamDialog)
        self.phaseBCurrentDoubleSpinBox.setGeometry(QtCore.QRect(200, 80, 62, 22))
        self.phaseBCurrentDoubleSpinBox.setMaximum(999.0)
        self.phaseBCurrentDoubleSpinBox.setObjectName("phaseBCurrentDoubleSpinBox")
        self.label_7 = QtWidgets.QLabel(voltageCurrentWeightParamDialog)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 54, 22))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(voltageCurrentWeightParamDialog)
        self.label_8.setGeometry(QtCore.QRect(140, 110, 54, 22))
        self.label_8.setObjectName("label_8")
        self.phaseCVoltageDoubleSpinBox = QtWidgets.QDoubleSpinBox(voltageCurrentWeightParamDialog)
        self.phaseCVoltageDoubleSpinBox.setGeometry(QtCore.QRect(70, 110, 62, 22))
        self.phaseCVoltageDoubleSpinBox.setMaximum(999.0)
        self.phaseCVoltageDoubleSpinBox.setObjectName("phaseCVoltageDoubleSpinBox")
        self.phaseCCurrentDoubleSpinBox = QtWidgets.QDoubleSpinBox(voltageCurrentWeightParamDialog)
        self.phaseCCurrentDoubleSpinBox.setGeometry(QtCore.QRect(200, 110, 62, 22))
        self.phaseCCurrentDoubleSpinBox.setObjectName("phaseCCurrentDoubleSpinBox")
        self.label_10 = QtWidgets.QLabel(voltageCurrentWeightParamDialog)
        self.label_10.setGeometry(QtCore.QRect(10, 110, 54, 22))
        self.label_10.setObjectName("label_10")
        self.okPushButton = QtWidgets.QPushButton(voltageCurrentWeightParamDialog)
        self.okPushButton.setGeometry(QtCore.QRect(50, 150, 75, 23))
        self.okPushButton.setObjectName("okPushButton")
        self.cancelPushButton = QtWidgets.QPushButton(voltageCurrentWeightParamDialog)
        self.cancelPushButton.setGeometry(QtCore.QRect(160, 150, 75, 23))
        self.cancelPushButton.setObjectName("cancelPushButton")

        self.retranslateUi(voltageCurrentWeightParamDialog)
        QtCore.QMetaObject.connectSlotsByName(voltageCurrentWeightParamDialog)

    def retranslateUi(self, voltageCurrentWeightParamDialog):
        _translate = QtCore.QCoreApplication.translate
        voltageCurrentWeightParamDialog.setWindowTitle(_translate("voltageCurrentWeightParamDialog", "分量参数"))
        self.label.setText(_translate("voltageCurrentWeightParamDialog", "分量Mask"))
        self.label_2.setText(_translate("voltageCurrentWeightParamDialog", "A相电压"))
        self.label_3.setText(_translate("voltageCurrentWeightParamDialog", "A相电流"))
        self.label_5.setText(_translate("voltageCurrentWeightParamDialog", "B相电流"))
        self.label_7.setText(_translate("voltageCurrentWeightParamDialog", "B相电压"))
        self.label_8.setText(_translate("voltageCurrentWeightParamDialog", "C相电流"))
        self.label_10.setText(_translate("voltageCurrentWeightParamDialog", "C相电压"))
        self.okPushButton.setText(_translate("voltageCurrentWeightParamDialog", "确定"))
        self.cancelPushButton.setText(_translate("voltageCurrentWeightParamDialog", "取消"))
