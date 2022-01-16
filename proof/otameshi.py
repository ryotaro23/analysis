import pyvisa


rm = pyvisa.ResourceManager
#つながれている装置のリストを得る
print(rm.list_resources())
#つながれている装置をリスト(配列) visa_listへ代入
visa_list=rm.list_resources()

#visa_list[0]これをusb1とする
#visa_list[3]これをusb2とする
usb1=visa_list[0]
usb2=visa_list[3]

#usb1につながっている装置名を出力 DMM(Keithley)であることが分かる
inst1=rm.open_resource(usb1)
print(inst1.query("*IDN?"))
#usb2につながっている装置名を出力 電源(GWinstek)であることが分かる
inst2=rm.open_resource(usb2)
print(inst2.query("*IDN?"))
