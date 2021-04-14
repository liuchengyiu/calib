from calib.comSerial.triphase import triphase_run
from calib.lib import *
from calib.comSerial.jc import jc_run
import time, math

def int_to_bcd(data: str)-> list:
    data_list=[]
    a= 0
    b= 0
    for i in data:
        if i == ".":
            continue
        if len(data_list) % 2 == 0 and a==0:
            data_list.append(ten_to_2(int(i)))
            a+=1
            continue
        if b % 2 == 0:
            data_list.append(ten_to_2(int(i)))
        else:
            data_list[a] = data_list[a] + ten_to_2(int(i))
            a += 1
        b += 1
    return data_list

def int_relative(jc, power, gap) -> bool:
    jc= float(jc)
    power= float(power)
    resuln= jc- power
    if power * gap > math.fabs(resuln):
        return str(round(resuln/power*100, 4)) + '%'
    else:
        return False


def jc_relative_power(jc_dict: dict, power_list: list) -> bool:
    result= []
    if len(jc_dict) == 0 and len(power_list) == 0:
        return False
    result.append(int_relative(jc_dict['40'], power_list[0], 0.002))
    result.append(int_relative(jc_dict['43'], power_list[1]* 0.001, 0.002))
    result.append(int_relative(jc_dict['50'], power_list[2], 0.005))
    result.append(int_relative(jc_dict['41'], power_list[6], 0.002))
    result.append(int_relative(jc_dict['44'], power_list[7]*0.001, 0.002))
    result.append(int_relative(jc_dict['51'], power_list[8], 0.005))
    result.append(int_relative(jc_dict['42'], power_list[12], 0.002))
    result.append(int_relative(jc_dict['45'], power_list[13]*0.001, 0.002))
    result.append(int_relative(jc_dict['52'], power_list[14], 0.005))
    print(result)
    for res in result:
        if res.find('False') != -1:
            print("error too big")
            return False

    print("calibration pass")
    return True


send_tr_list=[
    ["68", "01"],  # 三相四线
    ["68", "07", "01110000", "00100010", "00100000", "00000000", "00000000", "00000000"],  # 电压220
    ["68", "07", "01110001", "00100000", "00000001", "01010000", "00000000", "00000000"],  # 电流1.5
    ["68", "03"],  # 打开功能
    ["68", "07", "01110011", "00100000", "01100000", "00000000"],  # 功率因数0.5L
    ["68", "0a"],  # 读电压结果
    ["68", "07", "01110001", "00100000", "00000000", "00000111", "01010000", "00000000"],  # 电流0.075
    ["68", "07", "01110001", "00100000", "00000000", "00000000", "00000000", "00000000"],  # 电流0
    ["68", "07", "01110011", "00100000", "00000000", "00000000"],  # 功率因数1
    ["68", "0b"],  # 读功率结果
    ["68", "05"],  # 关闭功能
    ["68", "07", "01110001", "00100000", "00000000", "01010000", "00000000", "00000000"],  # 电流0.5
    ["68", "07", "01110001", "00100000", "00000000", "00000101", "00000000", "00000000"],  # 电流0.05
    ["68", "07", "01110001", "00100000", "00000000", "00000001", "00000000", "00000000"],  # 电流0.01
]
def runCaLib(ser_triphase, ser_jc, mainWindow):
    if triphase_run(ser_triphase, send_tr_list[0]) == False:
        return False
    triphase_run(ser_triphase, send_tr_list[1])
    triphase_run(ser_triphase, send_tr_list[2])
    triphase_run(ser_triphase, send_tr_list[3])
    triphase_run(ser_triphase, send_tr_list[8])
    time.sleep(3)
    read_data = batebcd_to_int(triphase_run(ser_triphase, send_tr_list[5]))
    if read_data == False or round(float(read_data["40"])) != 220 or round(float(read_data["43"]), 1) != 1.5:
        return False
    jc_run(ser_jc, {}, 1, 1)
    time.sleep(1)
    jc_run(ser_jc, {'temp': '25'}, 5, 1)
    jc_run(ser_jc, read_data, 6, 1)

    jc_run(ser_jc, {'1': '0.075', '2': '0.015'}, 19, 1)  # 相位分段补偿设置
    triphase_run(ser_triphase, send_tr_list[11])  # 0.5A
    triphase_run(ser_triphase, send_tr_list[4])  # 0.5L
    time.sleep(3)
    read_data = batebcd_to_int(triphase_run(ser_triphase, send_tr_list[5]))
    jc_run(ser_jc, read_data, 7, 0.5)  # 发送相位校正帧

    triphase_run(ser_triphase, send_tr_list[12])  # 0.05A
    time.sleep(3)
    read_data = batebcd_to_int(triphase_run(ser_triphase, send_tr_list[5]))
    jc_run(ser_jc, read_data, 7, 0.5)  # 发送相位校正帧

    triphase_run(ser_triphase, send_tr_list[13])  # 0.01A
    time.sleep(3)
    read_data = batebcd_to_int(triphase_run(ser_triphase, send_tr_list[5]))
    jc_run(ser_jc, read_data, 7, 0.5)  # 发送相位校正帧
    triphase_run(ser_triphase, send_tr_list[6])  # 开始功率校正
    time.sleep(3)
    read_data = batebcd_to_int(triphase_run(ser_triphase, send_tr_list[5]))
    if read_data == False or round(float(read_data["43"]), 3) != 0.075:
        return False
    jc_run(ser_jc, read_data, 8, 0.5)
    triphase_run(ser_triphase, send_tr_list[7])
    time.sleep(3)
    jc_run(ser_jc, {}, 9, 0.5)
    triphase_run(ser_triphase, send_tr_list[1])
    triphase_run(ser_triphase, send_tr_list[2])
    triphase_run(ser_triphase, send_tr_list[8])
    time.sleep(3)
    read_data = batebcd_to_int(triphase_run(ser_triphase, send_tr_list[5]))
    if read_data == False or round(float(read_data["40"])) != 220 or round(float(read_data["43"]), 1) != 1.5:
        return False
    jc_run(ser_jc, read_data, 10, 1)
    jc_run(ser_jc, {'1': '55', '2': '4'}, 4, 1)  # 启动阈值设置

    jc_run(ser_jc, {}, 11, 1)  # 结束校表

    triphase_dict = dict(batebcd_to_int(triphase_run(ser_triphase, send_tr_list[5])),
                         **batebcd_to_int(triphase_run(ser_triphase, send_tr_list[9])))
    jc_read_data = jcread_to_int(jc_run(ser_jc, {}, 16, 1))
    print(triphase_dict, jc_read_data)
    return jc_relative_power(triphase_dict, jc_read_data)

def seartCaLib(mainWindow):
    ser_jc = mainWindow.Com
    ser_triphase = mainWindow.powerCom
    result= runCaLib(ser_triphase, ser_jc, mainWindow)
    if result == False:
        jc_run(ser_jc, {}, 11, 1)  # 结束校表
        mainWindow.autoLabel.setText("校表失败")
        print('校表失败')
    else:
        mainWindow.autoLabel.setText("校表成功")
        print('校表成功')