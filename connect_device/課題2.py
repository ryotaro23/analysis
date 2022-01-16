import pyvisa 
import time 
 
 
rm = pyvisa.ResourceManager() 
#  つながれている装置のリストを得る 
visa_list=rm.list_resources() 
# visa_list[0]が DMM(Keithley)  これを usb1 とする 
# visa_list[3]が電源(GWinstek)  これを usb2 とする 
usb1=visa_list[0] 
usb2=visa_list[3] 
# print(rm.list_resources()) 
inst1=rm.open_resource(usb1) 
print(inst1.query("*IDN?")) 
inst2=rm.open_resource(usb2) 
print(inst2.query("*IDN?")) 
 
# DMM(Keithley)の初期化(write():文字列の書き込み)
inst1.write('*RST') 
# DMM(Keithley)のステイタスのリセット 
inst1.write('*CLS') 
#  単発測定に設定 
inst1.write('SAMP:COUN 1') 
#  直流電圧でオートレンジに設定 
inst1.write('SENS:VOLT:DC:RANGE:AUTO ON') 
#  電源(GWinstek)の初期化 
inst2.write('*RST')

#  電源(GWinstek)の電流設定を 1A に 
# この電流以下では電圧制御(CV)モードで動く 
inst2.write(':CHAN1:CURR 1.0') 
 
#  出力する電圧をキーボードから入力 
# vset はここでは文字列であることに注意(input():キーボードから入力した文字や数値を受け取るための関数) 
vset=input('Set Voltage ') 
 
#  電源(GWinstek)の電圧設定を vinput に 
inst2.write(':CHAN1:VOLT '+vset) 
#  電源(GWinstek)の出力を on に   
inst2.write(':OUTP:STAT 1') 
#  電圧測定までのタイムラグを作る 
time.sleep(0.7) 
#  電圧測定のコマンド送付  戻ってきた値（文字列）を values で受け取る 
values=inst1.query_ascii_values('MEAS:VOLT:DC?') 
# print(values)ではリストを出力  values[0]だけなので[数字]となる 
# print(values[0])では vaules[0]を出力するので数字のみとなる 
print('Set Voltage = ',vset) 
print('Observed Voltage = ',values[0]) 
 
       
# DMM をローカルモードに戻す 
inst1.write('system:local') 
#  電源(GWinstek)の出力を off に   
inst2.write(':OUTP:STAT 0') 
