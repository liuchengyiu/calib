from calib.lib.index import listPortName
from serial import PARITY_NONE, PARITY_EVEN, PARITY_ODD, PARITY_MARK, PARITY_SPACE
from serial import STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO
from serial import FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS
from PyQt5.QtWidgets import QMessageBox


def listComName(self):
    port_names = listPortName()
    self.clear()
    self.addItem('请选择', '')
    for port in port_names:
        self.addItem(port, port)


def listBaudRate(self):
    baudrate = [50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200]
    self.clear()
    self.addItem('请选择', '')
    for baud in baudrate:
        self.addItem(str(baud), baud)


def listStopBits(self):
    self.clear()
    self.addItem('请选择', '')
    sb = {
        '1': STOPBITS_ONE,
        '1.5': STOPBITS_ONE_POINT_FIVE,
        '2': STOPBITS_TWO
    }
    for key in sb:
        self.addItem(key, sb[key])


def listDataBits(self):
    self.clear()
    self.addItem('请选择', '')
    db = {
        '5': FIVEBITS,
        '6': SIXBITS,
        '7': SEVENBITS,
        '8': EIGHTBITS
    }
    for key in db:
        self.addItem(key, db[key])


def listParity(self):
    self.clear()
    self.addItem('请选择', '')
    p = {
        'None': PARITY_NONE,
        'Even': PARITY_EVEN,
        'ODD': PARITY_ODD,
        'Mark': PARITY_MARK,
        'Space': PARITY_SPACE
    }
    for key in p:
        self.addItem(key, p[key])


def openButton(self, mainWindow):
    try:
        self.setDisabled(True)
        flag = mainWindow.Com.isOpen()
        if flag is True:
            self.setText('关闭中')
        else:
            self.setText('打开中')

        if flag is True:
            if mainWindow.Com.closeCom() is False:
                QMessageBox.warning(self.parent(), '提示', '关闭端口失败')
            self.setEnabled(True)
            self.setText('打开端口')
        else:
            com = mainWindow.calibComComboBox.currentData()
            baud = mainWindow.calibBaudComboBox.currentData()
            stop_bits = mainWindow.calibStopBitsComboBox.currentData()
            parity = mainWindow.calibParityComboBox.currentData()
            data_bits = mainWindow.calibDataBitsComboBox.currentData()
            if com is None or baud is None or stop_bits is None or parity is None \
                    or data_bits is None:
                QMessageBox.critical(self.parent(), '提示', '端口信息错误')
                self.setEnabled(True)
                self.setText('打开端口')
                return
            result = mainWindow.Com.openCom(
                port_name=com,
                baud_rate=baud,
                stop_bits=stop_bits,
                parity=parity,
                data_bits=data_bits
            )
            if result is True:
                self.setEnabled(True)
                self.setText('关闭端口')
            if result is False:
                self.setEnabled(False)
                self.setText('打开串口')
                QMessageBox.critical(self.parent(), '提示', '端口打开失败')
    except Exception as e:
        print(e)

