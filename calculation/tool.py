#numpyとscipyの疎行列、pyplotをインポート
import numpy as np
from scipy import sparse
from matplotlib import pyplot as plt


# 運動エネルギー行列Kの関数定義
def calc_kin(x):
    h = x[1] - x[0]#隣り合う座標の間隔
    N = len(x)#配列ｘの長さ
    diag = 1.0 / h **2 * np . ones (N)#対角部分の一次元配列（開始位置k=0)
    off_diag = -0.5 / h **2 * np . ones ( N - 1)#非対角部分の一次元配列（開始位置k=1,-1)
    kin_term = sparse.diags ([diag,off_diag,off_diag],(0,-1,1))#3重対角行列
    return kin_term

# 波動関数のプロット関数定義
def plot (x,psi,eigval,xlbl,ylbl):
    #ラベル定義
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    #エネルギーの小さいものから３つ固有エネルギーのリスト作成
    energies = ['E = {:7.4f}'. format (eigval[i]) for i in range (3) ]
    #3つの固有状態に属する固有ベクトルをプロット
    plt . plot (x , psi [0] , color ='blue', label = energies [0])
    plt . plot (x , psi [1] , color ='green', label = energies [1])
    plt . plot (x , psi [2] , color ='red', label = energies [2])

    plt . legend ()#凡例を表示
    plt . show ()#はプロットを表示し続けその画面を消すまでスクリプト内のこの文以降の作業を行わない関数
    return plot
