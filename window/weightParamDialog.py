# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weightParamDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_weightParamDialog(object):
    def setupUi(self, weightParamDialog):
        weightParamDialog.setObjectName("weightParamDialog")
        weightParamDialog.resize(427, 212)
        self.label = QtWidgets.QLabel(weightParamDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 22))
        self.label.setObjectName("label")
        self.weightMaskSpinBox = QtWidgets.QSpinBox(weightParamDialog)
        self.weightMaskSpinBox.setGeometry(QtCore.QRect(70, 20, 61, 22))
        self.weightMaskSpinBox.setObjectName("weightMaskSpinBox")
        self.label_2 = QtWidgets.QLabel(weightParamDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 54, 22))
        self.label_2.setObjectName("label_2")
        self.phaseAVoltageDoubleSpinBox = QtWidgets.QDoubleSpinBox(weightParamDialog)
        self.phaseAVoltageDoubleSpinBox.setGeometry(QtCore.QRect(70, 50, 62, 22))
        self.phaseAVoltageDoubleSpinBox.setObjectName("phaseAVoltageDoubleSpinBox")
        self.phaseACurrentDoubleSpinBox = QtWidgets.QDoubleSpinBox(weightParamDialog)
        self.phaseACurrentDoubleSpinBox.setGeometry(QtCore.QRect(200, 50, 62, 22))
        self.phaseACurrentDoubleSpinBox.setObjectName("phaseACurrentDoubleSpinBox")
        self.label_3 = QtWidgets.QLabel(weightParamDialog)
        self.label_3.setGeometry(QtCore.QRect(140, 50, 54, 22))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(weightParamDialog)
        self.label_4.setGeometry(QtCore.QRect(270, 50, 71, 22))
        self.label_4.setObjectName("label_4")
        self.phaseAPowerFactorDoubleSpinBox = QtWidgets.QDoubleSpinBox(weightParamDialog)
        self.phaseAPowerFactorDoubleSpinBox.setGeometry(QtCore.QRect(350, 50, 62, 22))
        self.phaseAPowerFactorDoubleSpinBox.setObjectName("phaseAPowerFactorDoubleSpinBox")
        self.phaseBPowerFactorDoubleSpinBox = QtWidgets.QDoubleSpinBox(weightParamDialog)
        self.phaseBPowerFactorDoubleSpinBox.setGeometry(QtCore.QRect(350, 80, 62, 22))
        self.phaseBPowerFactorDoubleSpinBox.setObjectName("phaseBPowerFactorDoubleSpinBox")
        self.label_5 = QtWidgets.QLabel(weightParamDialog)
        self.label_5.setGeometry(QtCore.QRect(140, 80, 54, 22))
        self.label_5.setObjectName("label_5")
        self.phaseBVoltageDoubleSpinBox = QtWidgets.QDoubleSpinBox(weightParamDialog)
        self.phaseBVoltageDoubleSpinBox.setGeometry(QtCore.QRect(70, 80, 62, 22))
        self.phaseBVoltageDoubleSpinBox.setObjectName("phaseBVoltageDoubleSpinBox")
        self.phaseBCurrentDoubleSpinBox = QtWidgets.QDoubleSpinBox(weightParamDialog)
        self.phaseBCurrentDoubleSpinBox.setGeometry(QtCore.QRect(200, 80, 62, 22))
        self.phaseBCurrentDoubleSpinBox.setObjectName("phaseBCurrentDoubleSpinBox")
        self.label_6 = QtWidgets.QLabel(weightParamDialog)
        self.label_6.setGeometry(QtCore.QRect(270, 80, 71, 22))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(weightParamDialog)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 54, 22))
        self.label_7.setObjectName("label_7")
        self.phaseCPowerFactorDoubleSpinBox = QtWidgets.QDoubleSpinBox(weightParamDialog)
        self.phaseCPowerFactorDoubleSpinBox.setGeometry(QtCore.QRect(350, 110, 62, 22))
        self.phaseCPowerFactorDoubleSpinBox.setObjectName("phaseCPowerFactorDoubleSpinBox")
        self.label_8 = QtWidgets.QLabel(weightParamDialog)
        self.label_8.setGeometry(QtCore.QRect(140, 110, 54, 22))
        self.label_8.setObjectName("label_8")
        self.phaseCVoltageDoubleSpinBox = QtWidgets.QDoubleSpinBox(weightParamDialog)
        self.phaseCVoltageDoubleSpinBox.setGeometry(QtCore.QRect(70, 110, 62, 22))
        self.phaseCVoltageDoubleSpinBox.setObjectName("phaseCVoltageDoubleSpinBox")
        self.phaseCCurrentDoubleSpinBox = QtWidgets.QDoubleSpinBox(weightParamDialog)
        self.phaseCCurrentDoubleSpinBox.setGeometry(QtCore.QRect(200, 110, 62, 22))
        self.phaseCCurrentDoubleSpinBox.setObjectName("phaseCCurrentDoubleSpinBox")
        self.label_9 = QtWidgets.QLabel(weightParamDialog)
        self.label_9.setGeometry(QtCore.QRect(270, 110, 71, 22))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(weightParamDialog)
        self.label_10.setGeometry(QtCore.QRect(10, 110, 54, 22))
        self.label_10.setObjectName("label_10")
        self.okPushButton = QtWidgets.QPushButton(weightParamDialog)
        self.okPushButton.setGeometry(QtCore.QRect(110, 170, 75, 23))
        self.okPushButton.setObjectName("okPushButton")
        self.cancelPushButton = QtWidgets.QPushButton(weightParamDialog)
        self.cancelPushButton.setGeometry(QtCore.QRect(240, 170, 75, 23))
        self.cancelPushButton.setObjectName("cancelPushButton")

        self.retranslateUi(weightParamDialog)
        QtCore.QMetaObject.connectSlotsByName(weightParamDialog)

    def retranslateUi(self, weightParamDialog):
        _translate = QtCore.QCoreApplication.translate
        weightParamDialog.setWindowTitle(_translate("weightParamDialog", "分量参数"))
        self.label.setText(_translate("weightParamDialog", "分量Mask"))
        self.label_2.setText(_translate("weightParamDialog", "A相电压"))
        self.label_3.setText(_translate("weightParamDialog", "A相电流"))
        self.label_4.setText(_translate("weightParamDialog", "A相功率因素"))
        self.label_5.setText(_translate("weightParamDialog", "B相电流"))
        self.label_6.setText(_translate("weightParamDialog", "B相功率因素"))
        self.label_7.setText(_translate("weightParamDialog", "B相电压"))
        self.label_8.setText(_translate("weightParamDialog", "C相电流"))
        self.label_9.setText(_translate("weightParamDialog", "C相功率因素"))
        self.label_10.setText(_translate("weightParamDialog", "C相电压"))
        self.okPushButton.setText(_translate("weightParamDialog", "确定"))
        self.cancelPushButton.setText(_translate("weightParamDialog", "取消"))