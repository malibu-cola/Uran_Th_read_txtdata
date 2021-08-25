import csv

file = open("sample.csv", "w")
w = csv.writer(file)
w.writerow(["青森", "apple", 120])
file.close()