from PyQt5.QtWidgets import QComboBox
import types


def setShowPopUp(combobox, beforeShowPopUp) -> QComboBox:
    def showPopUp(self):
        self.beforeShowPopUp()
        self.backShowPopUp()
    combobox.backShowPopUp = types.MethodType(showPopUp, combobox)
    combobox.backShowPopUp = combobox.showPopup
    combobox.beforeShowPopUp = types.MethodType(beforeShowPopUp, combobox)
    combobox.showPopup = types.MethodType(showPopUp, combobox)
    combobox.showPopup()
    return combobox


def setMousePressEvent(combobox, beforeMousePressEvent) -> QComboBox:
    def mousePressEvent_(self, *args):
        self.beforeMousePressEvent()
        self.showPopup()
    combobox.beforeMousePressEvent = types.MethodType(beforeMousePressEvent, combobox)
    combobox.mousePressEvent = types.MethodType(mousePressEvent_, combobox)
    return combobox


def setHidePopUp(combobox, beforeHidePopUp) -> QComboBox:
    def hidePopUp(self):
        self.beforeHidePopUp()
        self.backHidePopUp()
    combobox.backHidePopUp = types.MethodType(hidePopUp, combobox)
    combobox.backHidePopUp = combobox.hidePopup
    combobox.beforeHidePopUp = types.MethodType(beforeHidePopUp, combobox)
    combobox.hidePopup = hidePopUp
    return combobox


def HocCombobox(combobox, beforeShowPopUp=None, beforeMousePressEvent=None, beforeHidePopUp=None) -> QComboBox:
    if beforeMousePressEvent is not None:
        combobox = setMousePressEvent(combobox=combobox, beforeMousePressEvent=beforeMousePressEvent)
    if beforeShowPopUp is not None:
        combobox = setShowPopUp(combobox=combobox, beforeShowPopUp=beforeShowPopUp)
    if beforeHidePopUp is not None:
        combobox = setHidePopUp(combobox=combobox, beforeHidePopUp=beforeHidePopUp)
    return combobox
