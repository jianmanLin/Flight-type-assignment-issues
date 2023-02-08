import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

def read_data(filename):
    data_set = pd.read_csv(filename)
    return data_set

'''
首先要剔除所有非数值数据
在通过fit计算出每一个特征的平均值，用transform对缺失值进行填充
再构造成pd.DataFrame
data_set--数据集合
drop_name--非数值型列名
'''
def data_drop_in(data_set, drop_name):
    impute = SimpleImputer(strategy='median')
    data_set_num = data_set.drop(drop_name, axis=1)
    #fit
    impute.fit(data_set_num)
    # print(impute.statistics_)
    #对指定数据进行transfrom
    X = impute.transform(data_set_num)
    data_new = pd.DataFrame(X, columns=data_set_num.columns, index=data_set_num.index.values)
    return data_new

'''
将字符型特征序列化
两种形式的转换-自行选择
data_set--要做数据处理的数据集
noNum_name--数据为非数值型的列名
'''
def data_noNum_transform(data_set, noNum_name):
    ordinal_encoder = OrdinalEncoder()
    #有两个括号
    data_cat = data_set[noNum_name]
    data_cat_encoder = ordinal_encoder.fit_transform(data_cat)
    # print(data_cat_encoder)

    #
    cat_encoder = OneHotEncoder()
    data_cat_1hot = cat_encoder.fit_transform(data_cat)
    # print(data_cat_1hot.toarray())
    return data_cat_encoder


'''
使用pipeline完成一个流水线任务
data_set_num--数据为数值型
'''
def num_pipline(data_set_num):
    #数值型特征
    pipeline = Pipeline([('impute', SimpleImputer(strategy='median')),
              ('std_scaler', StandardScaler())])

    data_num_tr = pipeline.fit_transform(data_set_num)

    return data_num_tr, pipeline

'''
data_set--要做数据处理的数据集
data_set_num--数据为数值型的列名
data_cat--数据为字符型的列名
pipeline--做数值数据处理的流水线
'''
def all_pipline(data_set, data_set_num, data_cat, pipeline):

    full_pipeline = ColumnTransformer([('num', pipeline, data_set_num),
                       ('cat', OrdinalEncoder(), data_cat)])

    data_set_new = full_pipeline.fit_transform(data_set)
    return data_set_new

    # print(data_set_new)


if __name__ == '__main__':
    filename = 'dataSet/iris.csv'
    data_set = read_data(filename)
    # print(data_set)
    data_drop_in = data_drop_in(data_set, 'Species')
    # print(data_drop_in)
    data_noNum_transform = data_noNum_transform(data_set, 'Species')
    # print(data_noNum_transform)
    data_num, pipeline = num_pipline(data_set.drop('Species', axis=1))
    # print(pipeline)
    # print(data_num)
    data_num_list = list(data_drop_in)
    data_noNum_list = ['Species']
    data_all_new = all_pipline(data_set, data_num_list, data_noNum_list, pipeline)
    print(data_all_new)