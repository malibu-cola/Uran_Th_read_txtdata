import os
import glob
import linecache

Ye = ["001", "005", "010", "015", "020", "025", "030"]
T = ["9", "10", "11"]
rho = ["8", "9", "10", "11", "12", "13"]


for x in Ye:
    for y in T:
        for z in rho:
            path = "./txtdata/Ye_" + x + "_T_1e" + y + "_rho_1e" + z + ".txt"
            target_line = linecache.getline(path,6127)
            element, Z, A, N, mass, solarMF, MF,InitialMF = target_line.split()
            print("Ye:", x, " T:1e", y, "rho:1e", z,"  ", MF, "  ")
            # print(target_line.split())
            linecache.clearcache()