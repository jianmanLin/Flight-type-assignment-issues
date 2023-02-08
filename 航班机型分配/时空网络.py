import numpy as np
# import xlwt
import pandas as pd
import matplotlib.pyplot

import Sklearn_data_anly.Sklearn_数据处理模块
from Sklearn_data_anly import *


data = pd.read_csv('data_set/data_fam_schedule.csv')
# print(data.head())

# data_noNum = data[['origin', 'destination']]
# print(data_noNum.head())

data_noNum_transforms = Sklearn_data_anly.Sklearn_数据处理模块.data_noNum_transform(data, ['origin', 'destination'])
# print(data_noNum_transforms)

origin = data_noNum_transforms[:, 0]
destination = data_noNum_transforms[:, 1]
#获得将机场地点数据化的数据集
data['origin'] = origin
data['destination'] = destination

origin_set = np.array(list(set(origin)))
origin_set = origin_set.astype(np.int)
destination_set = np.array(list(set(destination)))
destination_set = destination_set.astype(np.int)

# print(origin_set)
# print(destination_set)

#各个机场的所属航班
airport_flight_out = []
airport_flight_small = []
data_origin = np.array(data['origin'])
data_destination = np.array(data['destination'])
# 获得从机场i出发的航班索引
for i in origin_set:
    for j in range(data.shape[0]):
        if data_origin[j] == i:
            airport_flight_small.append(j)
    airport_flight_out.append(airport_flight_small)
    airport_flight_small = []

# print(airport_flight_out)

#获得从机场i进入的航班索引
airport_flight_in = []

for i in destination_set:
    for j in range(data.shape[0]):
        if data_destination[j] == i:
            airport_flight_small.append(j)
    airport_flight_in.append(airport_flight_small)
    airport_flight_small = []

# print('===========================================================')
# print(airport_flight_in)

#获得从机场i进入和出发的航班索引
# airport_flight_all = []
# airport_flight_out = []
# airport_flight_in = []
# for i in origin_set:
#     for j in range(data.shape[0]):
#         if data_origin[j] == i:
#             airport_flight_out.append(j)
#         if data_destination[j] == i:
#             airport_flight_in.append(j)
#     airport_flight_all.append(airport_flight_in + airport_flight_out)
#     # break
#     airport_flight_in = []
#     airport_flight_out = []

# print(airport_flight_all)


# print(airport_flight_all)

data_time_out = data['deptime'] - data['depoff']
data_time_in = data['arrtime'] - data['arroff']
data['time_off'] = data_time_out
data['time_arr'] = data_time_in
# print(data)


#将各个机场所有航班的起飞时间和降落时间按时间标准排序
airport_flight_time_index_sort = []
airport_flight_time_values_sort = []
for i in origin_set:
    out_index = airport_flight_out[i]
    in_index = airport_flight_in[i]
    data_all = pd.concat([data_time_in[in_index], data_time_out[out_index]])
    # print(data_all.sort_values().index.tolist())
    # print(data_all.sort_values())
    airport_flight_time_index_sort.append(data_all.sort_values().index.tolist())
    airport_flight_time_values_sort.append(data_all.sort_values().values.tolist())

    # print(airport_flight_time_sort)
    # break
# print(airport_flight_time_index_sort)
# print(airport_flight_time_values_sort)
# df_values = pd.DataFrame(airport_flight_time_values_sort)
# df_values.to_csv('机场时间排序')

# print(airport_flight_time_values_sort)
# print(airport_flight_time_index_sort)
#将各个机场所有航班的起飞时间和降落时间按时间标准进行编号--1，2，3......
m = 0
airport_flight_number_small = []
airport_flight_number = []
for i in airport_flight_time_index_sort:
    for j in range(len(i)):
        airport_flight_number_small.append(m)
        m = m + 1
    airport_flight_number.append(airport_flight_number_small)
    airport_flight_number_small = []

# print(airport_flight_number)
# print(airport_flight_number)

#定义终止节点
airport_flight_end = []
for i in airport_flight_number:
    end = len(i) - 1
    airport_flight_end.append(i[end])

# print(airport_flight_end)
# print(len(airport_flight_end))

#用于判断出港还是进港航班---  1-进  -1-出
a_in_out = []
a_in_out_all = []

for i in origin_set:
    for j in range(len(airport_flight_number[i])):
        # print(airport_flight_time_sort[i][j])
        #获取该航班的标号索引
        index = airport_flight_time_index_sort[i][j]
        if data['time_off'][index] == airport_flight_time_values_sort[i][j]:
            a_in_out.append(-1)
        else:
            a_in_out.append(1)
    a_in_out_all.append(a_in_out)
    a_in_out = []

# print(a_in_out_all)



'''
a_m_k--航班k在节点m处为出港航班为-1， 为进港航班为1
'''
m = airport_flight_number
# print(m)
k = airport_flight_time_index_sort
# print(k)
result = a_in_out_all
# print(result)
index = 0
a_m_k = np.zeros([1630, 815])
T_m_i = np.zeros([1630, 815])
airport_index = np.zeros([1630, 815])
# print(a_m_k)
for i in origin_set:
    for j in range(len(m[i])):
        col = airport_flight_time_index_sort[i][j]
        a_m_k[index, col] = result[i][j]
        T_m_i[index, col] = airport_flight_time_values_sort[i][j]
        airport_index[index, col] = airport_flight_time_index_sort[i][j]
        index += 1




# print(a_m_k[:, 37])
df = pd.DataFrame(a_m_k)
df_time = pd.DataFrame(T_m_i)
df_index = pd.DataFrame(airport_index)
df_index.to_csv('航班节点索引.csv')
df_time.to_csv('航班节点时间.csv')
df.to_csv('航班时空网络plot')





'''
写入excel表
'''
# # book0 = xlwt.Workbook(encoding='utf-8', style_compression=0)
# sheet1 = book0.add_sheet('航班网络', cell_overwrite_ok=True)
# col = ([i for i in range(len(a_in_out_all))])
# print(col)
#
# for i in col:
#     sheet1.write(0, i, col[i])
#
# #所在列
# for j in col:
#     data = a_in_out_all[j]
#     #所在行
#     for i in range(len(a_in_out_all[j])):
#         sheet1.write(i + 1, j, data[i])
#
# save_path = 'D:/py_to_excel/航班网络.xls'
# book0.save(save_path)
#
#
# # book1 = xlwt.Workbook(encoding='utf-8', style_compression=0)
# sheet2 = book0.add_sheet('航班网络班号', cell_overwrite_ok=True)
# col = ([i for i in range(len(a_in_out_all))])
#
# for i in col:
#     sheet2.write(0, i, col[i])
#
# #所在列
# for j in col:
#     data = airport_flight_time_index_sort[j]
#     #所在行
#     for i in range(len(a_in_out_all[j])):
#         sheet2.write(i + 1, j, data[i])
#
# save_path1 = 'D:/py_to_excel/航班网络班号.xls'
# book0.save(save_path1)




