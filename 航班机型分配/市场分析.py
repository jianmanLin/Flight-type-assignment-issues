import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data_set/市场.csv')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['font.sans-serif'] = ['SimHei']###解决中文乱码
plt.rcParams['axes.unicode_minus'] = False

Host_share_re = np.array(data['Host_share'], dtype=np.float)
Host_share_pr = np.array(data['6'], dtype=np.float)


plt.style.use('seaborn-pastel')

plt.ylim(0, 5)
plt.scatter(np.arange(len(Host_share_pr)), Host_share_pr)
plt.plot(np.arange(len(Host_share_pr)), Host_share_pr)

plt.scatter(np.arange(len(Host_share_pr)), Host_share_re)
plt.plot(np.arange(len(Host_share_pr)), Host_share_re)
plt.show()