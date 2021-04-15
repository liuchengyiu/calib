import serial
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtWidgets
from calib.lib.index import listPortName, int4_to_float, trans_to_16, batebcd_to_int, jcread_to_int
import threading
from time import sleep
from calib.comSerial.triphase import triphase_run
from calib.comSerial.jc import jc_run
from calib.comSerial.run import jc_relative_power, send_tr_list


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
        # text = com.parent.frameTextEdit.toPlainText()
        # print(len(text))
        # if len(text) > 4000:
        #     com.parent.frameTextEdit.setText("")
        com.recode('rx', frame_)
        com.readCache = trans_to_16(frame_)
        eventMaster(com, frame_)
        i = i + length
    com.container = com.container[i:]

def powerData(com, data):
    for d in data[:]:
        com.container.append(d)
    i = 0
    container = com.container

    if len(container) < 5:
        return
    while i < len(container):
        if container[i] != 104:
            i = i + 1
            continue
        if (i + 2) >= len(container):
            break
        length = container[i+2]+ 5
        if i + length > 300:
            i = i + 1
            continue
        if i + length > len(container):
            break
        frame_ = container[i:i + length]
        if frame_[-1] != 22:
            i = i + 1
            continue
        com.recode('rx', frame_)
        com.readCache = trans_to_16(frame_)
        i = i + length
    com.container = com.container[i:]


def eventMaster(com, frame):
    if frame[3] == 0 or frame[3] == 0x0f:
        deal00Frame(com, frame)
    elif frame[3] == 144:
        result= ['', '', '', '', '', '']
        try:
            triphase_dict = dict(batebcd_to_int(triphase_run(com.parent.powerCom, send_tr_list[5])),
                                 **batebcd_to_int(triphase_run(com.parent.powerCom, send_tr_list[9])))
            jc_read_data = jcread_to_int(com.readCache[1:])
            print(triphase_dict, '\r\n', jc_read_data)
            result = jc_relative_power(triphase_dict, jc_read_data, 1)
            print(result)
        except Exception as e:
            print("三相串口未连接", e)

        for i in range(3):
            updateTable(com, 0, i + 1, frame, ((i * 6) + 1) * 4, result[i * 2 + 1])
            updateTable(com, 1, i + 1, frame, ((i * 6) + 2) * 4, result[i * 2 + 1])
            updateTable(com, 2, i + 1, frame, ((i * 6) + 3) * 4, result[i * 2 + 1])
            updateTable(com, 3, i + 1, frame, ((i * 6) + 4) * 4, '')
            updateTable(com, 4, i + 1, frame, ((i * 6) + 5) * 4, '')
            updateTable(com, 5, i + 1, frame, ((i * 6) + 6) * 4, '')

        for i in range(11):
            row = i
            if i >= 3:
                row = i +1
            updateTable(com, row+2, 0, frame, (i + 19) * 4, '')

    print(str(trans_to_16(frame)))



def updateTable(com, row, line, frame, sub, percent):
    data = int4_to_float([frame[sub +3], frame[sub + 2], frame[sub + 1], frame[sub]]);
    data = round(data, 5);
    if percent is None:
        com.parent.measuredValueTableWidget2.setItem(row, line, QtWidgets.QTableWidgetItem(str(data)+ '('+ percent +')'));
    else:
        com.parent.measuredValueTableWidget2.setItem(row, line,
                                                     QtWidgets.QTableWidgetItem(str(data)));
    com.parent.measuredValueTableWidget2.viewport().update();


def deal00Frame(com, frame):
    # print('rx', frame, 'aaa=', frame[3])
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
    if frame[4] == 19:
        com.parent.phaseSubsectionResultLabel.setText(status)
    if frame[4] == 4:
        com.parent.startPriceResultLabel.setText(status)
    return


def readData(com, power):
    while True:
        if com.exit is True:
            break
        if com.isOpen() is False:
            sleep(0.1)
            continue
        data = com.com.read(1)
        if len(data) != 0:
            if power == "power":
                powerData(com, data)
            else:
                dealData(com, data)


class Com:
    def __init__(self, parent, power):
        self.com = serial.Serial()
        self.parent = parent
        self.readCache = ''
        self.container = []
        self.exit = False
        try:
            self.deal_thread = threading.Thread(target=readData, args=(self, power))
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

