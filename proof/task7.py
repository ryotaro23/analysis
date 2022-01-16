from matplotlib import pyplot#matplotlibを読み込む
import numpy as np

tlist=[]
x1list=[]#計算
x2list=[]#解析解
#代入
x1=5
x2=0
v=0
a=0
b=1
k=1
m=1
dt=0.01
i=1
while i<=1000:#繰り返し
    t=dt*i
    x1=x1+v*dt
    v=v+(-k*x1-b*v)*dt/m
    x2=(5*np.exp(-t))*(np.cos(t)+np.sin(t))
    tlist.append(t)
    x1list.append(t)
    x2list.append(t)
#プロット
pyplot.plot(t, x1, color = 'red')
pyplot.plot(t, x2, color = 'blue',  linestyle = '--')
pyplot.title('graph')
pyplot.xlabel('t[s]')
pyplot.ylabel('x[m]')
pyplot.show()

    
