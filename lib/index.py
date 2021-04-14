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



def int4_to_float(array) -> float:
    data = bytearray()
    if len(array) < 4:
        return False
    for i in range(4):
        if array[i] >= 256:
            return False
        data.append(array[i])
    return struct.unpack("!f", data)[0]

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

def two_to_10(bate: int) -> int:
    bate = int(bin(bate).replace("0b", ""));
    return bate

def two_to_16(bate: int) -> str:
    bate = hex(int(str(bate),2)).replace("0x", "");
    if len(bate) == 1:
        bate = "0"+ bate
    return bate

def twoBcd_to_16(bate: str) -> str:
    bate_high= bate[:4];
    bate_low = bate[4:];
    bate= hex(int(bate_high, 2)).replace("0x", "")+ hex(int(bate_low, 2)).replace("0x", "");
    bate= ten_to_16(51+ sixteen_to_10(bate));
    if len(bate) == 1:
        bate = "0"+ bate
    return bate

def sixteen_to_10(bate: str) -> int:
    if bate == "":
        return 0
    bate = int(bate, 16);
    return bate
def ten_to_16(bate: int) -> str:
    bate= hex(bate).replace("0x", "");
    if len(bate) == 1:
        bate = "0" + bate
    return bate

def ten_to_2(bate: int) -> str:
    bate = bin(bate).replace("0b", "");
    for i in range(3):
        if len(bate) <4:
            bate= "0"+ bate;
    return bate

def int4_to_float(array) -> float:
    data = bytearray()
    if len(array) < 4:
        return False
    for i in range(4):
        if array[i] >= 256:
            return False
        data.append(array[i])
    return struct.unpack("!f", data)[0]

def batebcd_to_int(data: str) -> dict:
    if data == False:
        return False
    send_jc_dict = {}
    data_list = data.split(" ")[3:-2]
    data_value = ""
    data_type = ""
    for i in range(len(data_list)):
        if data_list[i] == "33":
            continue
        if i == 0 or i % 9 == 0:
            data_value = ''
            data_type = ten_to_16(sixteen_to_10(data_list[i]) - sixteen_to_10("33"))
            continue
        else:
            data_int = sixteen_to_10(data_list[i]) - sixteen_to_10("63")
            if data_int == -2:
                data_int = '.'
            if data_int == -3:
                data_int = '-'
            data_value = data_value + str(data_int)
        if i % 8 != 0:
            send_jc_dict[data_type] = data_value
    return send_jc_dict

def jcread_to_int(data: str) -> list:
    data= data.split(" ")
    voltage_current = []
    for index, values in enumerate(data):
        data[index]= sixteen_to_10(values)
    if data[3] == 144:
        for i in range(29):
            voltage_current.append(round(int4_to_float([data[i * 4 + 7], data[i * 4 + 6], data[i * 4 + 5], data[i * 4 + 4]]), 5))
    return voltage_current