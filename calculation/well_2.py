#numpyとscipyの疎行列,sparse,calc_kin関数をインポート
import numpy as np
from scipy import sparse
from scipy . sparse . linalg import eigsh
from tool import calc_kin , plot

#ポテンシャル行列 V を作る関数を定義
def calc_pot (V0 , Nout , Nin ) :
    pot_out = V0 * np . ones ( Nout ) #井戸の外（片側）の各座標でのポテンシャルの値は V0
    pot_in = 0.0 * np . ones ( Nin ) #井戸の中ポテンシャルは 0
    pot = np . append ( pot_out , pot_in ) #：井戸の左側と井戸の中の各座標でのポテンシャルの値を表す 1 次元配列
    pot = np . append ( pot , pot_out ) #井戸の右側のポテンシャルの情報を追加
    pot_term = sparse . diags ( pot )#：pot を対角成分とする行列
    return pot_term

#計算

#ξn のリストの作成。
#座標の範囲
xi_max = 4
xi_min = - xi_max 
N = 400 #ξ の範囲を分ける
xi = np . linspace ( xi_min , xi_max , num =N ) #範囲内を等分し、配列に入れる

#ポテンシャル情報定義
V0 = 13.#ポテンシャルの深さ
Nin = int (N /( xi_max - xi_min )) #ポテンシャルの外の座標の個数を決定
Nout = int (N * ( xi_max - 1/2) /( xi_max - xi_min ) ) #ポテンシャルの内の座標の個数を決定
N = Nin + 2 * Nout

#hamに代入
ham = calc_kin ( xi )
ham = ham + calc_pot (V0 , Nout , Nin )

#Hの対角化
neig = 20 #固有値の個数
eigval , eigvec = eigsh ( ham , k= neig , which = 'SM')#固有値と固有ベクトルを計算
eigvec = eigvec .T#固有ベクトルの配列 eigvec を転置

#出力
print ( eigval [0:3]) #最低エネルギーから3つの固有値エネルギー
plot (xi , eigvec , eigval ,'x/L', 'psi')#固有ベクトルを表示
