from PyQt5.QtWidgets import QPushButton
import types


def setBeforeClick(button, beforeClick, MainWindow) -> QPushButton:
    button.clicked.connect(lambda: beforeClick(button, MainWindow))
    return button


def setButtonToolTip(button, message) -> QPushButton:
    button.setToolTip(message)
    return button


def HocPushButton(button, MainWindow, beforeClick=None, tool_tip=None) -> QPushButton:
    if beforeClick is not None:
        button = setBeforeClick(button, beforeClick=beforeClick, MainWindow=MainWindow)
    if tool_tip is not None:
        button = setButtonToolTip(button, message=tool_tip)
    return button
