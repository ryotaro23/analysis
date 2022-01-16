#numpyとscipyの疎行列,sparse,calc_kin関数をインポート
import numpy as np
from scipy import sparse
from scipy . sparse . linalg import eigsh
from tool import calc_kin , plot

#関数を定義
def calc_pot ( xi ):
    pot = 0.5 * ( xi **2)#各座標でのポテンシャルエネルギーを計算し1 次元配列
    pot_term = sparse . diags ( pot )#ポテンシャル行列
    return pot_term

#計算

#ξn のリストの作成。
#座標の範囲
xi_max = 4
xi_min = - xi_max 
N = 400 #ξ の範囲を分ける
xi = np . linspace ( xi_min , xi_max , num =N ) #範囲内を等分し、配列に入れる


#hamに代入
ham = calc_kin ( xi )
ham = ham + calc_pot (xi)

#Hの対角化
neig = 20 #固有値の個数
eigval , eigvec = eigsh ( ham , k= neig , which = 'SM')#固有値と固有ベクトルを計算
eigvec = eigvec .T#固有ベクトルの配列 eigvec を転置

#出力
print ( eigval [0:3]) #最低エネルギーから3つの固有値エネルギー
plot (xi , eigvec , eigval ,'xi', 'psi')#固有ベクトルを表示
