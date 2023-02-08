import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['font.sans-serif'] = ['SimHei']###解决中文乱码
plt.rcParams['axes.unicode_minus'] = False


dataSet = pd.read_csv('data_set/data_fam_products.csv')
# print(dataSet.info())

drop_list = ['Origin', 'Destination', 'Flight1', 'Flight2', 'Flight3', 'Class', 'Fare']
dataSet_RD = dataSet.drop(drop_list, axis=1)
print(dataSet_RD.head())
# print(dataSet_RD)
RD_matrix = np.array(dataSet_RD)
# print(RD_matrix.shape)
RD_matrix_sum = np.sum(RD_matrix, axis=0)
print(RD_matrix_sum)
# x = np.arange(31)
# plt.figure(figsize=(12, 12 ))
# plt.grid(ls='--')
# plt.tick_params(labelsize=7)
# colors = RD_matrix_sum# 随机产生50个用于颜色映射的数值
# sizes = RD_matrix_sum*0.1  # 随机产生50个用于改变散点面积的数值
# plt.scatter(x, RD_matrix_sum, marker='*', c=colors, s=sizes, alpha=0.6, cmap='viridis')
# plt.plot(x, RD_matrix_sum, linestyle=':', label='距离开机前N天的机票小时量')
# plt.colorbar()
# plt.xlabel('距离飞机起飞第 N 天')
# plt.ylabel('销售量')
# plt.xticks(x)
# plt.show()




dataSet_RD_columns = dataSet_RD.columns
# print(dataSet_RD_columns)
dataSet_out = np.sum(dataSet_RD, axis=1)
dataSet_out_matrix = np.array(dataSet_out)
#各个等级的销售情况
# print(dataSet_out.shape)

count = 0
list = []
dataSet_out_all = []
for i in range(1, len(dataSet_out)+1):
    if i % 11 == 0:
        k = i - 11
        # print(k)
        dataSet_out_all.append(np.sum(dataSet_out[k : i]))
        list = dataSet['flight'][k]

dataSet_out_all_matrix = np.array(dataSet_out_all)
# print(list)
#各个航班的销售情况

# print(dataSet_out_all_matrix.shape)


data_fare = dataSet['Fare']
data_fare_matrix = np.array(data_fare)
#每个各个等级的收入
data_class_fare = data_fare_matrix * dataSet_out_matrix.T
data_class_fare_matrix = np.array(data_class_fare)
# print(data_class_fare.shape)

#每个航班的收入
# data_class_fare_all = []
# for i in range(1, len(dataSet_out)+1):
#     if i % 11 == 0:
#         k = i - 11
#         # print(k)
#         data_class_fare_all.append(np.sum(data_class_fare[k : i]))
#
# data_class_fare_all = np.array(data_class_fare_all)
# # print(data_class_fare_all.shape)
#
# data_flight1 = dataSet['Flight1']
# data_flight2 = dataSet['Flight2']
# data_flight3 = dataSet['Flight3']
#
# B_index = []
# A_index = []
#
# for i in range(len(dataSet_out)):
#     if data_flight1[i][0:1] == 'B' or data_flight2[i][0:1] == 'B' or data_flight3[i][0:1] == 'B':
#         B_index.append(i)
#     else:
#         A_index.append(i)
# B_index_matrix = np.array(B_index)
# A_index_matrix = np.array(A_index)
# # print(A_index_matrix.shape)
# # print(B_index_matrix.shape)
#
#
# dataSet_out_A = data_class_fare_matrix[A_index]
# dataSet_out_B = data_class_fare_matrix[B_index]
# print(np.sum(dataSet_out_A))
# print(np.sum(dataSet_out_B))
# print(np.sum(data_class_fare))