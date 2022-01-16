import pyvisa
import time


rm = pyvisa.ResourceManager()
# つながれている装置のリストを得る
visa_list=rm.list_resources()
# visa_list[0]がDMM(Keithley) これをusb1とする
# visa_list[3]が電源(GWinstek) これをusb2とする
usb1=visa_list[0]
usb2=visa_list[3]
# print(rm.list_resources())
inst1=rm.open_resource(usb1)
print(inst1.query("*IDN?"))
inst2=rm.open_resource(usb2)
print(inst2.query("*IDN?"))

# DMM(Keithley)の初期化
inst1.write('*RST')
# DMM(Keithley)のステイタスのリセット
inst1.write('*CLS')
# 単発測定に設定
inst1.write('SAMP:COUN 1')

# 電源(GWinstek)の初期化
inst2.write('*RST')

# 電源(GWinstek)の電流設定を1Aに
#         この電流以下では電圧制御(CV)モードで動く
inst2.write(':CHAN1:CURR 1.0')

# 出力する電圧をキーボードから入力
# vsetはここでは文字列であることに注意
vset=input('Set Voltage ')

#float関数を使って文字列を浮動小数点数値に変換したのち場合分け
if float(vset) >= 1:
    inst1.write('SENS:CURR:DC:RANGE:AUTO ON')    
else:
    inst1.write('SENS:VOLT:DC:RANGE:1')


# 電源(GWinstek)の電圧設定をvinputに
inst2.write(':CHAN1:VOLT '+vset)
# 電源(GWinstek)の出力をonに 
inst2.write(':OUTP:STAT 1')
# 電圧測定までのタイムラグを作る
time.sleep(0.7)
# 電圧測定のコマンド送付 戻ってきた値（文字列）をvaluesで受け取る
values=inst1.query_ascii_values('MEAS:VOLT:DC?')
# print(values)ではリストを出力 values[0]だけなので[数字]となる
# print(values[0])ではvaules[0]を出力するので数字のみとなる
print('Set Voltage = ',vset)
print('Observed Voltage = ',values[0])

