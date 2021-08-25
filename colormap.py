from numpy.core.fromnumeric import reshape
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

list_2d = [[0,1,2],[3,4,5]]
# plt.figure()
# sns.heatmap(list_2d)
# plt.savefig("./sample.png")
# plt.close("all")

# arr_2d = np.arange(-8,8).reshape((3,4))
# print(arr_2d)
# plt.figure()
# sns.heatmap(arr_2d)
# plt.savefig("./sample2.png")

df = pd.DataFrame(data = list_2d, index = ["1e9", "1e10"], columns = ["1e8", "1e9","1e10"])
print(df)
plt.figure()
sns.heatmap(df)
plt.savefig("./sample3.png")