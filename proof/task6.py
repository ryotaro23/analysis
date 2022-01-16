from matplotlib import pyplot
import numpy as np
tlist = []
xlist = []


#代入
x=1#初期位置
k=1#ばね定数
m=1#質量
dt=0.01#時間微小変化
v=0#初速度
for i in range(10000):#1000回繰り返す
    t=i*dt
    v=v-(k/m)*x*dt
    x= np.cos((k/m)**(1/2)* t)
    xlist.append(x)
    tlist.append(t)
    i=i+1
pyplot.plot(tlist, xlist, color = 'red')
pyplot.title('graph')
pyplot.xlabel('t[s]')
pyplot.ylabel('x[m]')
pyplot.show()

    
