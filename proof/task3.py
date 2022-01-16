c = 1 # 初期濃度 / 任意単位
import numpy as np#expをライブラリに組み込む
dt = 0.01 # Δt / s
k = 0.5 # 速度定数 / s^-1
i = 1
while i <= 1000:# 10 s 分の計算
    c = np.exp(-k * i * dt)
    print(i, i*dt, c)
    i = i + 1
