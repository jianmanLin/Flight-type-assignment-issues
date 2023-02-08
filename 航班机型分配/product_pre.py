import numpy as np
import pandas as pd
from Sklearn_data_anly import Sklearn_数据处理模块
data_product = pd.read_csv('data_set/data_fam_products.csv')
data_market = pd.read_csv('data_set/data_fam_market_share.csv')


drop_list = ['Origin', 'Destination', 'Flight1', 'Flight2', 'Flight3', 'Class', 'Fare']

data_RD = data_product.drop(drop_list, axis=1)
data_RD = np.sum(data_RD, axis=1)
data_product_OD = Sklearn_数据处理模块.data_noNum_transform(data_product, ['Origin', 'Destination'])


data = pd.DataFrame()
data['O'] = data_product_OD[:, 0]
data['D'] = data_product_OD[:, 1]
data['Sum'] = data_RD
data['market_share'] = np.zeros(data.shape[0])
data_tran = np.zeros([data_product.shape[0], 1])
# print(data)
for i in range(data_product.shape[0]):
    if data_product['Flight2'][i] == '.' and data_product['Flight3'][i] == '.':
        data_tran[i] = 1
    if data_product['Flight2'][i] != '.' and data_product['Flight3'][i] == '.':
        data_tran[i] = 2
    if data_product['Flight2'][i] != '.' and data_product['Flight3'][i] != '.':
        data_tran[i] = 3

data['transfort'] = data_tran

data_m = Sklearn_数据处理模块.data_noNum_transform(data_market, ['Org', 'Des'])
data_market.iloc[:, 0] = data_m[:, 0]
data_market.iloc[:, 1] = data_m[:, 1]

for i in range(data_product.shape[0]):
    if data['market_share'][i] != 0:
        continue
    for j in range(data_market.shape[0]):
        if data['O'][i] == data_market['Org'][j] and data['D'][i] == data_market['Des'][j]:
            data.loc[i, 'market_share'] = data_market['Host_share'][j]
            break

data.to_csv('data_set.csv')