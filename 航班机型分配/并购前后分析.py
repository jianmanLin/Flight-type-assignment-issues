import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['font.sans-serif'] = ['SimHei']###解决中文乱码
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv('data_set/data_fam_products.csv')


drop_list = ['Origin', 'Destination', 'Flight1', 'Flight2', 'Flight3', 'Class', 'Fare']

data_RD = data.drop(drop_list, axis=1)
data_RD = np.sum(data_RD, axis=1)
# print(data_RD)
data_RD_fare = np.array(data['Fare']) * np.array(data_RD)
data['RD_sum'] = data_RD_fare

A_index = []
B_index = []
for i in data.index:
    if data['Flight1'][i][:1] == 'B' or data['Flight2'][i][:1] == 'B' or data['Flight3'][i][:1] == 'B':
        B_index.append(i)
    else:
        A_index.append(i)

# print(len(A_index))
# print(len(B_index))

A_data = data.iloc[A_index]
B_data = data.iloc[B_index]
# print(A_data.head())
# print(B_data.head())

Class_list = ['B', 'G', 'H', 'K', 'L', 'M', 'Q', 'S', 'T', 'V', 'Y']
A_Class_list_fare = {}
B_Class_list_fare = {}
Class_list_fare = {}
for i in Class_list:
    A_Class_list_fare[i] = np.sum(A_data['RD_sum'][A_data['Class'] == i])

for i in Class_list:
    B_Class_list_fare[i] = np.sum(B_data['RD_sum'][B_data['Class'] == i])

for i in Class_list:
    Class_list_fare[i] = np.sum(data['RD_sum'][data['Class'] == i])

# print(A_Class_list_fare)
# print(B_Class_list_fare)
# print(Class_list_fare)
values = Class_list_fare.values()
values_list = np.array(list(values))
values = np.array(list(values)) * -1
values = list(values)


# plt.figure(figsize=(8, 12))
# plt.grid(ls='--')
# plt.bar(Class_list, A_Class_list_fare.values(), facecolor='#9999ff', edgecolor='white', label='并购前')
# plt.bar(Class_list, values, facecolor='#ff9999', edgecolor='white', label='并购后')
# for x, y in zip(Class_list, A_Class_list_fare.values()):
#     plt.text(x, y+1, int(y), ha='center', va='bottom')
#     # 数据显示的横坐标、显示的位置高度、显示的数据值的大小
# for x, y in zip(Class_list, values):
#     plt.text(x, y-10, int(-y), ha='center', va='top')
# plt.legend()
# plt.xlabel('各个舱位等级')
# plt.ylabel('各个舱位等级销售额')
# plt.xticks()

#
plt.figure(figsize=(8, 12))
plt.grid(ls='--')
x = list(range(len(values_list)))
total_width, n = 0.8, 2
width = total_width / n
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.-0.2, 1.03*height, '%s' % int(height))

a = plt.bar(x, A_Class_list_fare.values(), width=width, facecolor='#9999ff', label='并购前')
for i in range(len(x)):
    x[i] = x[i] + width
b = plt.bar(x, values_list, width=width, label='并购后', facecolor='#ff9999', tick_label=Class_list)


# for x, y in zip(Class_list, A_Class_list_fare.values()):
#     plt.text(a, y, int(y), ha='center', va='bottom')
#     # 数据显示的横坐标、显示的位置高度、显示的数据值的大小
#
# for x, y in zip(Class_list, values):
#     plt.text(a, y, int(-y), ha='center', va='bottom')
plt.legend()
autolabel(a)
autolabel(b)
plt.xlabel('各个舱位等级')
plt.ylabel('各个舱位等级销售额')
plt.xticks()
plt.show()


