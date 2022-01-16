import random # random ライブラリを組み込む
number=10000000
c=0
i=1
while i<=number:#試行回数10000回
    x=random.random()#x座標の決定
    y=random.random()#y座標の決定
    if x**2+y**2<=1:#半径１の円に入るか判別
        c=c+1
    i=i+1
print(number,c)
pi=4*c/number#円周率の定義
print(pi)
