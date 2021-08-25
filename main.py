# やりたいこと
# 温度を縦軸、密度を横軸、存在量を色分けしてウランの存在量マップを作りたい。
# とりあえず、すべてのファイルからウランの存在量のデータを持ちたい。
# このとき、ファイルネームから温度と密度のデータも持っておきたい。

import os
import glob
import linecache
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

Ye = ["001", "005", "010", "015", "020", "025", "030"]
T = ["9", "10", "11"]
rho = ["8", "9", "10", "11", "12", "13"]

# テキストファイルからウラン238のMFを読み込み、配列に入れていく
m = 0
n = 0
for x in Ye:
    graph = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    n = 0
    for y in T:
        m = 0
        for z in rho:
            path = "./txtdata/Ye_" + x + "_T_1e" + y + "_rho_1e" + z + ".txt"
            target_line = linecache.getline(path,6127) # 元素の行を探して入れる Th232:5912, U235:6124,  Uran238:6127, 
            element, Z, A, N, mass, solarMF, MF,InitialMF = target_line.split()
            print("Ye:", x, " T:1e", y, "rho:1e", z,"  ", MF, "  ")
            # print(target_line.split())
            if MF == "NaN":
                MF = '0.0'
            ret = float(MF)
            print(m, n, ret)
            graph[m][n] = ret
            linecache.clearcache()
            m+=1
        n += 1
    
    df = pd.DataFrame(data = graph, index = ["1e8", "1e9","1e10","1e11","1e12", "1e13"], columns = ["1e9", "1e10", "1e11"])
    print(df)
    plt.figure()
    sns.heatmap(df, annot=True)
    plt.savefig("./uran238/Ye_" + x + ".png")# 保存場所
    plt.close('all')