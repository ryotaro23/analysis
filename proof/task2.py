x=0#初期位置の設定
import random# random ライブラリを組み込む
from matplotlib import pyplot#matplotlibを読み込む
xlist=[]#xの値を記録する受け皿
s=1000#試行回数の定義
t=30#歩数の定義
i=0#試行回数の変数定義
j=0#歩数の変数定義
for i in range(0,s): #試行くりかえし
    for j in range(0,t):#酔歩くりかえし
        n=random.random()
        if n<=0.5:#向きの決定
            x=x+1
        else:
            x=x-1
        j=j+1#歩数を増やす
    xlist.append(x)#xの値を記録
    x=0#値のリセット
    j=0#値のリセット
    i=i+1#試行回数をふやす
pyplot.hist(xlist, range = (-t,t), bins = 2 * t + 1)
pyplot.title('simulation')
pyplot.xlabel('x axis')
pyplot.ylabel('y axis')
pyplot.show()

        



