import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['font.sans-serif'] = ['SimHei']###解决中文乱码
plt.rcParams['axes.unicode_minus'] = False

data_flight_num_0 = pd.read_excel('data_set/结果分析数据.xlsx', sheet_name='飞机使用架数')
data_flight_num_1 = pd.read_excel('data_set/结果分析数据.xlsx', sheet_name='飞机机型使用次数')
data_flight_num_2 =pd.read_excel('data_set/结果分析数据.xlsx', sheet_name='航班乘客量')
data_market = pd.read_csv('data_set/data_fam_market_share.csv')

temp = pd.read_csv('data_set/最大旅客量_.csv')
temp = temp['最大旅客量plot']

data_flight_num_2.loc['销售量'] = temp

#
# y = [0, 2, 9, 11, 4, 38, 10, 29, 48]
# plt.style.use('seaborn-pastel')
# plt.figure(figsize=(12, 8))
# plt.grid(ls='--')
# plt.tick_params(labelsize=7)
# line1, = plt.plot(data_flight_num_0['机型'], y, linestyle=':', label='飞机使用架数')
# plt.scatter(data_flight_num_0['机型'], y, marker='o', c='#87CEFA')
# plt.bar(data_flight_num_0['机型'], y)
# plt.legend(handles=[line1], labels=['架数'], loc='upper left')
# # plt.colorbar()
# plt.ylabel('使用架数', fontsize=20)
# plt.xlabel('机型名称', fontsize=20)
# plt.xticks(data_flight_num_0['机型'])
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)
# plt.show()


# plt.style.use('seaborn-pastel')
# plt.figure(figsize=(12, 8))
# plt.grid(ls='--')
# plt.tick_params(labelsize=7)
# line1, = plt.plot(data_flight_num_1['机型'], data_flight_num_1['次数'], linestyle=':', label='飞机使用次数')
# plt.scatter(data_flight_num_1['机型'], data_flight_num_1['次数'], marker='o', c='#87CEFA')
# plt.bar(data_flight_num_1['机型'], data_flight_num_1['次数'])
# plt.legend(handles=[line1], labels=['次数'], loc='upper left')
# # plt.colorbar()
# plt.ylabel('飞机使用次数', fontsize=20)
# plt.xlabel('机型名称', fontsize=20)
# plt.xticks(data_flight_num_0['机型'])
# plt.show()

# print(data_flight_num_2)


#
plt.style.use('seaborn-pastel')
plt.figure(figsize=(20, 12))
plt.grid(ls='--')
plt.tick_params(labelsize=7)
colors = data_market['Host_share'][:80]# 随机产生50个用于颜色映射的数值
sizes = 0.009 * data_market['Host_share'][:80]  # 随机产生50个用于改变散点面积的数值

x = np.arange(80)

line1, = plt.plot(x, data_market['Host_share'][:80], linestyle=':', label='航线市场额占比')
plt.scatter(x, data_market['Host_share'][:80], marker='o', c=colors, s=sizes, alpha=0.6)
plt.bar(x, data_market['Host_share'][:80])
plt.legend(handles=[line1], labels=['Host_share'][:-1], loc='upper left')
# plt.colorbar()
plt.ylabel('航线市场额占比', fontsize=20)
plt.xlabel('航线', fontsize=20)
plt.xticks(x)
plt.xticks(fontsize=13)
plt.show()
