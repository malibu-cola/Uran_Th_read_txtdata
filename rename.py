import os
import glob

Ye = ["001", "005", "010", "015", "020", "025", "030"]
T = ["9", "10", "11"]
rho = ["8", "9", "10", "11", "12", "13"]


for x in Ye:
    for y in T:
        for z in rho:
            path = "./txtdata/Ye" + x + "/T_1e" + y + "_rho_1e" + z
            path2 = "./txtdata/Ye_" + x + "_T_1e" + y + "_rho_1e" + z +".txt"
            os.rename(path,path2)


# path = "./txtdata/Ye010/T_1e11_rho_1e"
# i = 2
# j = 1
# flist = glob.glob(path)
# print('変更前')
# print(flist)


# for file in flist:
#    os.rename(file,'./txtdata/T_1e' str(9 + j % 3) '_rho_1e' + str(8 + i%6) + '.txt')
#    print(8 + i % 6)
#    print(9 + j % 3)
#    i += 1
    # i %= 6
    # if 8 + i 

# list = glob.glob(path1)
# print("変更後")
# print(list)