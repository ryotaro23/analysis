g = 9.8 # 重力加速度 / ms^-2
x = 0 # 初期座標 / m
v = 0 # 初速度 / ms^-1
dt = 0.01# Δt
i=0
while i<=1000:
    x = x + v*dt # この 2 行の
    v = v + g*dt # 計算の順序に注意
    print (i, i*dt, v, x)
    i=i+1

