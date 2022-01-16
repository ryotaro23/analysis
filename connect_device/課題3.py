import pyvisa
import time
import numpy as np
import matplotlib.pyplot as plt

rm = pyvisa.ResourceManager()
# つながれている装置のリストを得る
visa_list=rm.list_resources()
# visa_list[0]これをusb1とする
# visa_list[3]これをusb2とする
usb1=visa_list[0]
usb2=visa_list[3]
# print(rm.list_resources())
inst1=rm.open_resource(usb1)
print(inst1.query("*IDN?"))
inst2=rm.open_resource(usb2)
print(inst2.query("*IDN?"))

#DMM(Keithley)の初期化
inst1.write('*RST')
# DMM(Keithley)のステイタスのリセット
inst1.write('*CLS')
# DMM(Keithley)を単発測定に設定
inst1.write('SAMP:COUN 1')
# DMM(Keithley)を直流電圧でオートレンジに設定
inst1.write('SENS:CURR:DC:RANGE:AUTO ON')

# 電源(GWintek)の初期化
inst2.write('*RST')

# 電源(GWinstek)の電流設定を1Aに
#        この電流以下では電圧制御(CV)モードで動く
inst2.write(':CHAN1:CURR 1.0')

vst=input('Start Voltage Vst ')
ven=input('End Voltage Ven ')
vstep=input('Step Voltage Vstep ')
icount=int((float(ven)-float(vst))/float(vstep))


vval=[0]*(icount+1)
cval=[0]*(icount+1)


for i1 in range(icount+1):
   vinput=float(vst)+(i1)*float(vstep)
   vval[i1]=vinput


    
    # 電源(GWinstek)の電圧設定をvinputに
   inst2.write(':CHAN1:VOLT '+str(vinput))
    # 電源(GWinstek)の出力をonに
   inst2.write(':OUTP:STAT 1')
    # 電流測定までのタイムラグを作る
    #time.sleep(0.4)
    # 電流測定のコマンド送付 戻ってきた値を(文字リストの最初 values[0])で受け取る
   values=inst1.query_ascii_values('MEAS:CURR:DC?')
   cval[i1]=float(values[0])
   print('I= ',float(values[0]),'  R= ',vinput/float(values[0]))
    
# DMMをローカルモードに戻す
inst1.write('system:local')
# 電源(GWinstek)の出力をoffに 
inst2.write(':OUTP:STAT 0')
    
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.plot(vval, cval, marker="o", color = "red",linestyle = "--")
plt.show()
