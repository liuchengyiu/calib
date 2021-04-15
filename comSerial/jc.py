import binascii, time
import struct
def trans_floats_to_bytes(array) -> list:
    d = []
    for i in array:
        d.extend(trans_float_to_bytes(i))
    return d
def trans_float_to_bytes(data) -> bytes:
    return struct.pack('f', data)

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

def serial_send(serial, byte):
    print('jc_send=', binascii.b2a_hex(byte))
    serial.write(byte)

def serial_read(serial):
    data= serial.readCache[1:]
    print('jc_read==', data)
    if data[9:11] == '92':
        print('触发故障上报帧', data)
        return False
    if len(data) > 0 and data[:2] == "69" and data[-2:] == "43":
        return data
    else:
        return False

def dict_to_sixten(dict_data: dict, type, factor)-> str:
    data = []
    if type == 6 or type == 7 or type == 8 or type == 10:

        if type != 10:
            data = [float(dict_data['40']), round(float(dict_data['43']), 4), float(factor), float(dict_data['41']),
                    round(float(dict_data['44']), 4), float(factor), float(dict_data['42']),
                    round(float(dict_data['45']), 4), float(factor)]
        else:
            data = [float(dict_data['40']), round(float(dict_data['43']), 4), float(dict_data['41']),
                    round(float(dict_data['44']), 4), float(dict_data['42']), round(float(dict_data['45']), 4)]
        data = trans_floats_to_bytes(data)
        data.insert(0, 7)  # 插入分量Mask

    if type == 4:
        data = [float(dict_data['1']), float(dict_data['2'])]
        data = trans_floats_to_bytes(data)
    if type == 5:
        data = [float(dict_data['temp'])]
        data = trans_floats_to_bytes(data)
    send_data = createFrame(105, type, data, 67)
    return send_data



def jc_run(ser, send_list: dict, type, factor):
    serial_com = ser.com
    send_list= dict_to_sixten(send_list, type, factor)
    serial_com.flushInput()
    serial_send(serial_com, bytes(send_list))
    time.sleep(0.5)
    data = serial_read(ser)

    if not data:
        return False
    return data