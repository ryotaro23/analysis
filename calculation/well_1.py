#numpyとscipyの疎行列,calc_kin関数をインポート
import numpy as np
from scipy . sparse . linalg import eigsh
from tool import calc_kin , plot
#計算

#ξn のリストの作成。
#を井戸の内側 [−1/2, 1/2] とする
xi_max = 1/2
xi_min = - xi_max 
N = 50 #ξ の範囲を50個に分ける
xi = np . linspace ( xi_min , xi_max , num =N ) #範囲内を50個に等分し、配列に入れる

#hamに代入
ham = calc_kin ( xi )

#Hの対角化
neig = 20 #固有値の個数
eigval , eigvec = eigsh ( ham , k= neig , which = 'SM')#固有値と固有ベクトルを計算
eigvec = eigvec .T#固有ベクトルの配列 eigvec を転置

#出力
print ( eigval [0:3]) #最低エネルギーから3つの固有値エネルギー
plot (xi , eigvec , eigval ,'x/L', 'psi')#固有ベクトルを表示
