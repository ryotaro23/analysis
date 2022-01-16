#numpyとscipyの疎行列,sparse,calc_kin関数をインポート
import numpy as np
from scipy import sparse
from scipy . sparse . linalg import eigsh
from tool import calc_kin , plot

#ポテンシャルの計算する関数を定義
def calc_pot ( rho , l):
    coulomb = -1.0 / rho
    centrifugal = 0.5 * l * (l + 1) / rho **2
    coulomb_term = sparse . diags ( coulomb )
    centrifugal_term = sparse . diags ( centrifugal )
    pot_term = coulomb_term + centrifugal_term
    return pot_term
#計算

#座標定義
rho_max = 30 
N = 400 
rho = np . linspace ( rho_max , 0, num =N , endpoint = False ) # List of N discrete rho ’s

#hamに代入
l = 0
ham = calc_kin ( rho )
ham = ham + calc_pot (rho,l)

#Hの対角化
neig = 20 #固有値の個数
eigval , eigvec = eigsh ( ham , k= neig , which = 'SM')#固有値と固有ベクトルを計算
eigvec = eigvec .T#固有ベクトルの配列 eigvec を転置

#動径分布関数を計算
R2 = [( eigvec [i , :]) **2 for i in range ( len ( eigval ) )]

#出力
print ( eigval [0:3]) #最低エネルギーから3つの固有値エネルギー
plot (rho , R2 , eigval ,'rho/a0', 'R^2')#動径分布関数を表示
