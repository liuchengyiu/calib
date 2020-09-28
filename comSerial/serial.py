import serial
from PyQt5.QtGui import QTextCursor
from calib.lib.index import listPortName, trans_to_16
import threading
from time import sleep


def dealData(com, data):
    for d in data[:]:
        com.container.append(d)
    i = 0
    container = com.container
    if len(container) < 7:
        return
    while i < len(container):
        if container[i] != 105:
            i = i + 1
            continue
        if (i + 2) >= len(container):
            break
        length = container[i+1] + container[i+2]*256
        if i + length > 300:
            i = i + 1
            continue
        if i + length > len(container):
            break
        frame_ = container[i:i + length]
        if frame_[-1] != 67:
            i = i + 1
            continue
        text = com.parent.frameTextEdit.toPlainText()
        if len(text) > 5000:
            com.parent.frameTextEdit.setText('')
        com.recode('rx', frame_)
        eventMaster(com, frame_)
        i = i + length

    com.container = com.container[i:]


def eventMaster(com, frame):
    if frame[3] == 0 or frame[3] == 0x0f:
        deal00Frame(com, frame)
    print(trans_to_16(frame))


def deal00Frame(com, frame):
    status = ""
    if frame[3] == 0:
        status = "已发送"
        if frame[5] == 0:
            status = "发送失败"
    elif frame[3] == 0x0f:
        status = "执行成功"
        if frame[5] == 0:
            status = "执行失败"
    if frame[4] == 1:
        com.parent.statusLabel.setText(status)
    if frame[4] == 5:
        com.parent.TempResultLabel.setText(status)
    if frame[4] == 6:
        com.parent.powerGainCompensationResultLabel.setText(status)
    if frame[4] == 7:
        com.parent.phaseCorrectionResultLabel.setText(status)
    if frame[4] == 8:
        com.parent.powerOffsetResultLabel.setText(status)
    if frame[4] == 9:
        com.parent.powerRmsResultLabel.setText(status)
    if frame[4] == 10:
        com.parent.voltageCurrentGainResultLabel.setText(status)
    return


def readData(com):
    while True:
        if com.exit is True:
            break
        if com.isOpen() is False:
            sleep(0.1)
            continue
        data = com.com.read(1)
        if len(data) != 0:
            dealData(com, data)


class Com:
    def __init__(self, parent):
        self.com = serial.Serial()
        self.parent = parent
        self.container = []
        self.exit = False
        try:
            self.deal_thread = threading.Thread(target=readData, args=(self,))
            self.deal_thread.start()
        except Exception as e:
            print(e)

    def openCom(
            self,
            port_name='',
            baud_rate=9600,
            parity=serial.PARITY_NONE,
            stop_bits=serial.STOPBITS_ONE,
            data_bits=serial.FIVEBITS) -> bool:
        if port_name not in listPortName():
            print('com name is not exist')
            return False
        try:
            if self.com.isOpen() is True:
                self.com.close()
            self.com = serial.Serial(
                port=port_name,
                baudrate=baud_rate,
                parity=parity,
                stopbits=stop_bits,
                bytesize=data_bits)
        except Exception as e:
            print(e)
            return False
        return True

    def sendData(self, data) -> bool:
        if self.com.isOpen() is False:
            return False
        try:
            self.com.write(bytes(data))
        except Exception as e:
            return False
        self.recode('tx', data)
        return True

    def recode(self, t, frame):
        self.parent.frameTextEdit.append(t + ": " + trans_to_16(frame) + "\n")
        self.parent.frameTextEdit.moveCursor(QTextCursor.End)

    def closeCom(self) -> bool:
        if self.com.isOpen() is False:
            return True
        try:
            self.com.close()
        except Exception as e:
            print(e)
            return False
        return True

    def isOpen(self):
        return self.com.isOpen()

    def Exit(self):
        try:
            self.exit = True
        except Exception as e:
            print(e)

