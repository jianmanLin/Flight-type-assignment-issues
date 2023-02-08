import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['font.sans-serif'] = ['SimHei']###解决中文乱码
plt.rcParams['axes.unicode_minus'] = False


# data_airport_off = pd.read_excel('data_set/产品数据.xlsx', sheet_name='起始机场')
# data_airport_arr = pd.read_excel('data_set/产品数据.xlsx', sheet_name='降落机场')
# data_class = pd.read_excel('data_set/产品数据.xlsx', sheet_name='座位等级')
# data_fare = pd.read_csv('data_set/价格.csv')
# data_in_out = pd.read_excel('data_set/产品数据.xlsx', sheet_name='收购前后收益')
# data_time = pd.read_excel('data_set/产品数据.xlsx', sheet_name='出发时间')
data_RD = pd.read_csv('data_set/记录日.csv')


'''
RD
'''
plt.style.use('seaborn-pastel')
plt.figure(figsize=(20, 12))
plt.grid(ls='--')
plt.tick_params(labelsize=7)
colors = data_RD['销售量'][:-1]# 随机产生50个用于颜色映射的数值
sizes = 0.009 * data_RD['销售量'][:-1]  # 随机产生50个用于改变散点面积的数值

x = np.arange(len(data_RD['记录日'][:-1]))

line1, = plt.plot(x, data_RD['销售量'][:-1], linestyle=':', label='机票销售量')
plt.scatter(x, data_RD['销售量'][:-1], marker='o', c=colors, s=sizes, alpha=0.6)
plt.bar(x, data_RD['销售量'][:-1])
plt.legend(handles=[line1], labels=['机票销售量'][:-1], loc='upper left')
# plt.colorbar()
plt.ylabel('机票销售量', fontsize=20)
plt.xlabel('记录日', fontsize=20)
plt.xticks(x)
plt.show()


'''
data_airport_off = pd.read_excel('data_set/产品数据.xlsx', sheet_name='起始机场')--数据图
'''
# plt.style.use('seaborn-pastel')
# plt.figure(figsize=(20, 12))
# plt.grid(ls='--')
# plt.tick_params(labelsize=7)
# colors = data_airport_off['求和项:销售量'][:-1]# 随机产生50个用于颜色映射的数值
# sizes = 0.009 * data_airport_off['求和项:销售量'][:-1]  # 随机产生50个用于改变散点面积的数值
#
# x = np.arange(len(data_airport_off['起始机场'][:-1]))
#
# line1, = plt.plot(x, data_airport_off['求和项:销售量'][:-1], linestyle=':', label='机票销售量')
# plt.scatter(x, data_airport_off['求和项:销售量'][:-1], marker='o', c=colors, s=sizes, alpha=0.6, cmap='viridis')
# plt.bar(x, data_airport_off['求和项:销售量'][:-1])
# plt.legend(handles=[line1], labels=['机票销售量'][:-1], loc='upper left')
# # plt.colorbar()
# plt.ylabel('机票销售量', fontsize=20)
# plt.xlabel('出发机场编号', fontsize=20)
# plt.xticks(x)
#
# plt.figure(figsize=(20, 12))
# plt.grid(ls='--')
# plt.tick_params(labelsize=7)
# colors = data_airport_off['求和项:销售额'][:-1]# 随机产生50个用于颜色映射的数值
# sizes = 0.00009 * data_airport_off['求和项:销售额'][:-1]  # 随机产生50个用于改变散点面积的数值
# plt.scatter(x, data_airport_off['求和项:销售额'][:-1], marker='*', c=colors, s=sizes, alpha=0.6, cmap='viridis')
# line2, = plt.plot(x, data_airport_off['求和项:销售额'][:-1], linestyle=':', label='机票销售额')
# plt.bar(x, data_airport_off['求和项:销售额'][:-1])
# plt.legend(handles=[line2], labels=['机票销售额'][:-1], loc='upper left')
# # plt.colorbar()
# plt.xlabel('出发机场编号', fontsize=20)
# plt.ylabel('机票销售额', fontsize=20)
# plt.xticks(x)
# plt.show()

'''
data_airport_arr = pd.read_excel('data_set/产品数据.xlsx', sheet_name='降落机场')--数据图
'''
#
# plt.style.use('seaborn-pastel')
# plt.figure(figsize=(20, 12))
# plt.grid(ls='--')
# plt.tick_params(labelsize=7)
# colors = data_airport_arr['销售量'][:-1]# 随机产生50个用于颜色映射的数值
# sizes = 0.009 * data_airport_arr['销售量'][:-1]  # 随机产生50个用于改变散点面积的数值
# x = np.arange(len(data_airport_arr['降落机场'][:-1]))
#
# line1, = plt.plot(x, data_airport_arr['销售量'][:-1], linestyle=':', label='机票销售量')
# plt.scatter(x, data_airport_arr['销售量'][:-1], marker='o', c=colors, s=sizes, alpha=0.6, cmap='viridis')
# plt.legend(handles=[line1], labels=['机票销售量'], loc='upper left')
# plt.bar(x, data_airport_arr['销售量'][:-1])
# # plt.colorbar()
# plt.ylabel('机票销售量', fontsize=20)
# plt.xlabel('降落机场编号', fontsize=20)
# plt.xticks(x)

# plt.figure(figsize=(20, 12))
# plt.grid(ls='--')
# plt.tick_params(labelsize=7)
# colors = data_airport_arr['销售额'][:-1]# 随机产生50个用于颜色映射的数值
# sizes = 0.00009 * data_airport_arr['销售额'][:-1]  # 随机产生50个用于改变散点面积的数值
# plt.scatter(x, data_airport_arr['销售额'][:-1], marker='o', c=colors, s=sizes, alpha=0.6, cmap='viridis')
# line2, = plt.plot(x, data_airport_arr['销售额'][:-1], linestyle=':', label='机票销售额')
# plt.legend(handles=[line2], labels=['机票销售额'], loc='upper left')
# # plt.colorbar()
# plt.xlabel('降落机场编号', fontsize=20)
# plt.ylabel('机票销售额', fontsize=20)
# plt.xticks(x)
plt.show()

'''
data_fare = pd.read_excel('data_set/产品数据.xlsx', sheet_name='价格')
'''
#
# plt.style.use('seaborn-pastel')
# plt.figure(figsize=(12, 12))
# plt.subplot(121)
# plt.grid(ls='--')
# plt.tick_params(labelsize=12)
# x = data_fare['价格'][:-1]
# colors = data_fare['销售量'][:-1]
# sizes = 0.00009 * data_fare['销售量'][:-1]
# line1 = plt.scatter(x, data_fare['销售量'][:-1], marker='o', c=colors, s=sizes, alpha=0.6, cmap='viridis', label='各个价格区间的销售量')
# plt.bar(x, data_fare['销售量'][:-1])
# plt.plot(x, data_fare['销售量'][:-1], linestyle=':')
# # plt.colorbar()
# plt.xlabel('美元')
# plt.ylabel('销售量')
# plt.xticks(rotation=270)
# plt.legend(handles=[line1], labels=['各个价格区间的销售量'], loc='upper left')
#
#
# plt.subplot(122)
# plt.grid(ls='--')
# plt.tick_params(labelsize=12)
# colors = data_fare['销售额'][:-1]
# sizes = 0.00009 * data_fare['销售额'][:-1]
# # x = np.arange(0, 25, 4)
# line2 = plt.scatter(x, data_fare['销售额'][:-1], marker='o', c=colors, s=sizes, alpha=0.6, cmap='viridis', label='各个价格区间的销售额')
# plt.bar(x, data_fare['销售额'][:-1])
# plt.plot(x, data_fare['销售额'][:-1], linestyle=':')
# # plt.colorbar()
# plt.xlabel('美元')
# plt.ylabel('销售额')
# plt.xticks(rotation=270)
# plt.legend(handles=[line2], labels=['各个价格区间的销售额'], loc='upper left')
#
# plt.show()

'''
data_class = pd.read_excel('data_set/产品数据.xlsx', sheet_name='座位等级')
# '''

# plt.style.use('seaborn-pastel')
# plt.figure(figsize=(12, 12))
# plt.subplot(121)
# plt.grid(ls='--')
# plt.tick_params(labelsize=12)
# colors = data_class['销售额'][:-1]
# sizes = 0.00009 * data_class['销售额'][:-1]
# x = data_class['座位等级'][:-1]
# line1 = plt.scatter(x, data_class['销售量'][:-1], marker='o', c=colors, s=sizes, alpha=0.6, cmap='viridis', label='座位等级销售')
# plt.bar(x, data_class['销售量'][:-1])
# plt.plot(x, data_class['销售量'][:-1], linestyle=':')
# plt.xlabel('座位等级')
# plt.ylabel('销售量')
# # plt.colorbar()
# plt.legend(handles=[line1], labels=['座位等级销售'], loc='upper left')
#
#
# plt.subplot(122)
# plt.grid(ls='--')
# plt.tick_params(labelsize=12)
# colors = data_class['销售额'][:-1]
# sizes = 0.00009 * data_class['销售额'][:-1]
# x = data_class['座位等级'][:-1]
# line2 = plt.scatter(x, data_class['销售额'][:-1], marker='o', c=colors, s=sizes, alpha=0.6, cmap='viridis', label='座位等级销售')
# plt.bar(x, data_class['销售额'][:-1])
# plt.plot(x, data_class['销售额'][:-1], linestyle=':')
# # plt.colorbar()
# plt.xlabel('座位等级')
# plt.ylabel('销售额')
# plt.legend(handles=[line2], labels=['座位等级销售'], loc='upper left')
#
# plt.show()


'''
data_in_out = pd.read_excel('data_set/产品数据.xlsx', sheet_name='收购前后收益')
'''
# plt.style.use('seaborn-pastel')
# plt.figure(figsize=(7, 12))
# x = ['收购前', '收购后']
# plt.subplot(121)
# plt.bar(x, data_in_out['销售量'])
# plt.plot(x, data_in_out['销售量'],  linestyle=':', label='销售量')
# plt.xlabel('状态')
# plt.ylabel('销售量')
# plt.legend()
# plt.subplot(122)
# plt.bar(x, data_in_out['销售额'])
# plt.plot(x, data_in_out['销售额'],  linestyle=':', label='销售额')
# plt.xlabel('状态')
# plt.ylabel('销售额')
# plt.legend()
# plt.show()
# print(data_in_out['销售额'])

'''
data_tine = pd.read_excel('data_set/产品数据.xlsx', sheet_name='出发时间')
'''
# plt.style.use('seaborn-pastel')
#
# plt.figure(figsize=(12, 12))
# plt.subplot(121)
# plt.grid(ls='--')
# plt.tick_params(labelsize=12)
# x = data_time['出发时间'][:-1]
# colors = data_time['求和项:销售量'][:-1]
# sizes = 0.00009 * data_time['求和项:销售量'][:-1]
# line1 = plt.scatter(x, data_time['求和项:销售量'][:-1], marker='o', c=colors, s=sizes, alpha=0.6, cmap='viridis', label='各个时间的销售量')
# plt.bar(x, data_time['求和项:销售量'][:-1])
# plt.plot(x, data_time['求和项:销售量'][:-1], linestyle=':')
# # plt.colorbar()
# plt.xlabel('时间 / (小时)')
# plt.ylabel('销售量')
# plt.xticks(rotation=270)
# plt.legend(handles=[line1], labels=['各个时间的销售量'], loc='upper left')
#
#
# plt.subplot(122)
# plt.grid(ls='--')
# plt.tick_params(labelsize=12)
# colors = data_time['求和项:销售额'][:-1]
# sizes = 0.00009 * data_time['求和项:销售额'][:-1]
# # x = np.arange(0, 25, 4)
# line2 = plt.scatter(x, data_time['求和项:销售额'][:-1], marker='o', c=colors, s=sizes, alpha=0.6, cmap='viridis', label='各个时间的销售额')
# plt.bar(x, data_time['求和项:销售额'][:-1])
# plt.plot(x, data_time['求和项:销售额'][:-1], linestyle=':')
# # plt.colorbar()
# plt.xlabel('各个时间的销售额')
# plt.ylabel('销售额')
# plt.xticks(rotation=270)
# plt.legend(handles=[line2], labels=['各个时间的销售额'], loc='upper left')
#
# plt.show()