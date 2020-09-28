import serial.tools.list_ports as list_ports
import serial
import struct
from PyQt5.QtWidgets import QMessageBox
import inspect
import ctypes

frameMap = {
    "1": "启动校准",
    "2": "高频脉冲常数误差校准",
    "3": "失压阈值设置",
    "4": "启动阈值设置",
    "5": "温度校准",
    "6": "功率增益补偿",
    "7": "相位校正",
    "8": "功率offset校正",
    "9": "有效值校正",
    "a": "电压电流有效值增益校正",
    "b": "结束校正",
    "10": "实时数据采集",
    "21": "镜像传输开始",
    "22": "镜像分包传输",
    "23": "镜像传输结束"
}


def trans_to_16(data) -> str:
    result = ''
    for i in data:
        i_str = hex(i).replace('0x', '')
        if i < 16:
            result = result + ' 0' + i_str
        else:
            result = result + ' ' + i_str
    return result


def trans_float_to_bytes(data) -> bytes:
    return struct.pack('f', data)


def listPortName() -> set:
    device_name = set()
    for com in serial.tools.list_ports.comports():
        device_name.add(com.device)
    return device_name


def crc16_a001(data) -> int:
    crc16 = 0xFFFF
    for d in data:
        crc16 = crc16 ^ d
        for j in range(0, 8):
            if (crc16 & 0x01) > 0:
                crc16 = (crc16 >> 1) ^ 0xa001
                continue
            crc16 = crc16 >> 1
    return crc16


def createFrame(head, command, data, end) -> list:
    length = 7 + len(data)
    frame = [head, length & 0xFF, (length & 0xFF00) >> 8, command]
    for d in data:
        frame.append(d)
    crc = crc16_a001(frame)
    frame.append(crc & 0xFF)
    frame.append((crc & 0xFF00) >> 8)
    frame.append(end)
    return frame


def trans_floats_to_bytes(array) -> list:
    d = []
    for i in array:
        d.extend(trans_float_to_bytes(i))
    return d


def send_frame(frame, mainWindow):
    try:
        if mainWindow.Com.sendData(frame) is False:
            QMessageBox.critical(mainWindow, '提示', '发送失败')
            return
    except Exception as e:
        print(e)


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
