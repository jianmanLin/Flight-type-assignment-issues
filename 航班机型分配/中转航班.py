import pandas as pd
import numpy as np
import Sklearn_data_anly.Sklearn_数据处理模块
from Sklearn_data_anly.Sklearn_数据处理模块 import *
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('data_set/data_fam_products.csv')


drop_list = ['Origin', 'Destination', 'Flight1', 'Flight2', 'Flight3', 'Class', 'Fare']

data_RD = data.drop(drop_list, axis=1)
data_RD = np.sum(data_RD, axis=1)
data_RD_fare = np.array(data['Fare']) * np.array(data_RD)
data['RD_sum'] = data_RD_fare
data['中转次数'] = 1
# print(data)
#
for i in data.index:
    if data['Flight2'][i] != '.':
        data['中转次数'][i] += 1
    if data['Flight3'][i] != '.':
        data['中转次数'][i] += 1
data.to_csv('temp_data_')

# noNum_list = ['Origin', 'Destination']
# data_transfrom = Sklearn_data_anly.Sklearn_数据处理模块.data_noNum_transform(data, noNum_list)
# data['Origin'] = data_transfrom[:, 0]
# data['Destination'] = data_transfrom[:, 1]
# # print(len(data))
# data_array = np.array(data)
#
# # for i in range(0, len(data), 12):
# #     print(i)
# #     data_sum.append(data_RD[i])
# #     break
# data_sum_array = np.array(data_RD_fare)
# # print((data_sum_array[0:11]))
# data_sum_all = []
# j = 0
# for i in range(len(data)):
#     if i == 0:
#         data_sum_all.append((np.sum(data_sum_array[0:11])))
#     if i > 15 and i % 11 == 0:
#         j = i - 11
#         data_sum_all.append(np.sum(data_sum_array[j:i]))
#
# data_sum_all.append(np.sum(data_sum_array[47178:-1]))
# # print(data_sum_all)
# data_list = []
# for i in range(0, len(data), 11):
#     # print(i)
#     data_list.append(data.iloc[i])
#
# data_set = pd.DataFrame(data_list)
# data_set['RD_sum_all'] = data_sum_all
# # print(data_set)
# # print(data_set)
# # data_set.to_csv('独立产品')
# origin = set(data['Origin'])
# destination = set(data['Destination'])
# data_set['bool'] = 0
# data_set['bool'][0] = 1
#
# list = []
# for i in data_set.index:
#     if data_set['bool'][i] == 1:
#         continue
#     for j in data_set.index:
#         if data_set['bool'][j] == 1:
#             continue
#         if data_set['Origin'][i] == data_set['Origin'][j] and data_set['Destination'][i] == data_set['Destination'][j]:
#             list.append(i)
#             list.append(j)
#             data_set['bool'][i] = 1
#             data_set['bool'][j] = 1
#
# list_1 = []
# list_2 = []
# for i in data_set.index:
#     if data_set['Flight2'][i] != '.':
#         list_1.append(i)
#     if data_set['Flight3'][i] != '.':
#         list_2.append(i)

# print(list_1)
# print(list_2)
#
#
# print(len(list_1))
# print(len(set(list_2)))
# list_flight1 = []
# list_no_flight1 = []
#
# result_0 = []
# result_1 = []
# result_2 = []
# for i in data_set.index:
#     if i in list_1:
#        result_1.append(data_set['RD_sum_all'][i])
#     if i in list_2:
#         result_2.append(data_set['RD_sum_all'][i])
#     else:
#         result_0.append(data_set['RD_sum_all'][i])
#
# result_0 = np.sum(result_0)
# result_1 = np.sum(result_1)
# result_2 = np.sum(result_2)
#
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
# plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# plt.rcParams['font.sans-serif'] = ['SimHei']###解决中文乱码
# plt.rcParams['axes.unicode_minus'] = False
#
# x = ['直达', '中转一次', '中转两次']
# plt.figure(figsize=(8, 8))
# plt.plot(x, [result_0, result_1, result_2], linestyle=':', label='航班销售额')
# plt.scatter(x, [result_0, result_1, result_2], marker='o')
# plt.xlabel('')
# plt.ylabel('销售额')
# plt.legend()
# plt.show()
#
#
