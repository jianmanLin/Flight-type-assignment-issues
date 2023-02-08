import gurobipy
import numpy as np
import pandas as pd
np.set_printoptions(threshold=np.sys.maxsize)
from 时空网络 import *


def data_read(data_fleet, data_schedule, data_max_er):
    data_schedule['max_er'] = data_max_er['最大旅客量plot']
    aver_fare = np.array(data_max_er['Fare'])
    Z_ = pd.read_csv('data_set/旅客数量new.csv')

    # 获取飞行时间-- result_spand_time
    data_schedule['start_time'] = data_schedule['arrtime'] - data_schedule['arroff']
    data_schedule['end_time'] = data_schedule['deptime'] - data_schedule['depoff']
    start_time = np.array(data_schedule['start_time'])
    end_time = np.array(data_schedule['end_time'])
    result_start = np.zeros([815, 1])
    result_end = np.zeros([815, 1])
    result_spand_time = np.zeros([815, 1])

    for i in range(len(start_time)):
        X_1 = str(start_time[i])
        X_2 = str(end_time[i])
        if len(X_1) == 4:
            x1 = np.array(X_1[:2], dtype=float)
            y1 = np.array(float(X_1[2:])/60, dtype=float)
            result_start[i] = x1+y1
        else:
            x1 = np.array(X_1[:1], dtype=float)
            y1 = np.array(float(X_1[1:])/60, dtype=float)
            result_start[i] = x1 + y1
        if len(X_2) == 4:
            x2 = np.array(X_2[:2], dtype=float)
            y2 = np.array(float(X_2[2:]) / 60, dtype=float)
            result_end[i] = x2 + y2
        else:
            x2 = np.array(X_2[:1], dtype=float)
            y2 = np.array(float(X_2[1:]) / 60, dtype=float)
            result_end[i] = x2 + y2
        result_spand_time[i] = result_start[i] - result_end[i]
    #时间负数处理
    for i in range(result_spand_time.shape[0]):
        if result_spand_time[i] < 0:
            result_spand_time[i] = 24.00 + result_spand_time[i]

    # print(result_spand_time)



    # 获取每种机型的座位数目--S
    S = np.array(data_fleet['座位数'])
    # 获取每个机型每小时的飞行成本
    cost = np.array(data_fleet['每小时飞行成本']).reshape((1, 9))
    # 获取经停航班集合--print(flights)
    data_schedule['bool'] = 0
    flights_small = []
    flights = []
    for index_i, i in zip(data_schedule['flight'].index, data_schedule['flight']):
        if data_schedule['bool'][index_i] != 0:
            continue
        for index_j, j in zip(data_schedule['flight'][index_i + 1:].index, data_schedule['flight'][index_i + 1:]):
            if i == j and data_schedule['bool'][index_j] == 0:
                flights_small.append(index_j)
                data_schedule.loc[index_j, 'bool'] = 1
        if flights_small != []:
            flights_small.append(index_i)
            flights.append(flights_small)
            flights_small = []

    # 获取将机型j分配给航班i的费用
    C_i_j = np.zeros([815, 9])
    C_i_j = np.dot(result_spand_time, cost)
    # 机场节点时间
    flight_time = T_m_i
    # 机场节点航班号索引
    flight_index = k
    # 机场节点数量
    flight_m = airport_flight_number
    # 机场终止节点
    flight_m_end = airport_flight_end
    # 航班网络
    a_m_i = a_m_k
    # m节点机型j的数量
    G_m_j = {}
    # 各机型飞机数量
    N = np.array([39, 8, 9, 11, 4, 38, 10, 44, 48])
    # 航班最大顾客数量
    max_er = np.array(data_schedule['max_er'], dtype=int)
    max_er = max_er*0.85
    #每个航班的等级票价
    p = pd.read_csv('data_set/票价.csv')
    return flight_m, flight_m_end, a_m_i, G_m_j, max_er, C_i_j, flights, N, S, aver_fare, flight_time, flight_index, Z_, p



# def spill_anly(data_max_er):
#     # 旅客溢出
#     list_out = []
#     list_out_all = []
#     count = 0
#     for i in range(815):
#         if data_max_er.iloc[i]['最大旅客量'] > np.max(S):
#             list_out.append(data_max_er.iloc[i]['origin'])
#             list_out.append(data_max_er.iloc[i]['destination'])
#             list_out_all.append(list_out)
#             list_out = []
#     # print(list_out_all)
#     # 旅客不足
#     list_out_plot = []
#     list_out_all_plot = []
#     for i in range(815):
#         if data_max_er.iloc[i]['最大旅客量plot'] < np.min(S):
#             list_out_plot.append(data_max_er.iloc[i]['origin'])
#             list_out_plot.append(data_max_er.iloc[i]['destination'])
#             list_out_all_plot.append(list_out_plot)
#             list_out_plot = []
#     # print(list_out_all_plot)
#     matrix = np.zeros([len(list_out_all), len(list_out_all_plot)])
#     for index_i, i in enumerate(list_out_all):
#         for index_j, j in enumerate(list_out_all_plot):
#             if i == j:
#                 matrix[index_i, index_j] = 1
#     matrix_pd = pd.DataFrame(matrix)
#     matrix_pd.to_csv('matrix_new')
#

def print_result():
    result = pd.read_csv('model_out.csv')
    X_name = result['feature'][14670:22005]
    X_var = result['label'][14670:22005]
    result_matrix = np.zeros([815, 9])

    GE_name = result['feature'][31448:32204]
    GE_var = result['label'][31448:32204]

    GE_matrix = np.zeros([84, 9])

    #旅客
    Cu_mer_f = result['feature'][22483:31448]
    Cu_mer_l = result['label'][22483:31448]
    Cu_matrix = np.zeros([815, 11])


    index = 9
    for i in range(result_matrix.shape[0]):
        result_matrix[i, :] = X_var[index - 9:index]
        index += 9
    # print(np.array(result_matrix, dtype=int))
    fleet_use = np.sum(result_matrix, axis=0)
    print('各飞机的使用次数')
    print(fleet_use)
    count = 9
    for i in range(GE_matrix.shape[0]):
        GE_matrix[i, :] = GE_var[count - 9:count]
        count += 9
    print('使用架数')

    print(np.sum(GE_matrix, axis=0))
    # count_cu = 11
    # for i in range(Cu_matrix.shape[0]):
    #     Cu_matrix[i, :] = Cu_mer_l[count_cu - 11:count_cu]
    #     count_cu += 11
    # Z_result = pd.DataFrame(np.sum(Cu_matrix, axis=1))


    # print('旅客溢出航班数')
    # print(np.sum(cu_spill > 0))
    # print('旅客过少航班数')
    # print(np.sum(cu_spill < 0))


if __name__ == '__main__':
    data_fleet = pd.read_csv('data_set/data_fam_fleet.csv')
    data_schedule = pd.read_csv('data_set/data_fam_schedule.csv')
    data_max_er = pd.read_csv('data_set/最大旅客量_.csv')
    flight_m, flight_m_end, a_m_i, G_m_j, max_er, C_i_j, flights, N, S, Fare, T_m_i, airport_index, k, p = data_read(
        data_fleet, data_schedule, data_max_er)

    k = np.array(k)
    p = np.array(p, dtype=np.int)

#     '''
#     model part
#     '''

    model = gurobipy.Model('航班机型分配')
    X = {}
    y = {}
    spill = {}
    Z_i_m = {}
    numbers_i = len(data_schedule['flight'])
    numbers_j = len(data_fleet['机型'])

    # 添加决策变量
    for i in range(1630):
        for j in range(9):
            name = 'G_' + str(i) + '_' + str(j)
            G_m_j[i, j] = model.addVar(lb=0, ub=1000, vtype=gurobipy.GRB.INTEGER, name=name)
    for i in range(numbers_i):
        for j in range(numbers_j):
            name = 'X_' + str(i) + '_' + str(j)
            X[i, j] = model.addVar(lb=0, ub=1, vtype=gurobipy.GRB.BINARY, name=name)
    # 添加指示变量
    for j in range(numbers_j):
        for i in range(len(flights)):
            name = 'y_' + str(j) + str(i)
            y[j, i] = model.addVar(lb=0, ub=1, vtype=gurobipy.GRB.BINARY, name=name)
    z = model.addVar(lb=1, ub=1, vtype=gurobipy.GRB.INTEGER)

    # 旅客溢出率
    # for i in range(numbers_i):
    #     name = 'spill_' + str(i)
    #     spill[i] = model.addVar(lb=0, ub=0.5, vtype=gurobipy.GRB.CONTINUOUS, name=name)

    #航班i等级m的最大座位数，四舍五入
    for i in range(numbers_i):
        for j in range(11):
            name = 'Z_' + str(i) + '_' + str(j)
            Z_i_m[i, j] = model.addVar(lb=0, ub=np.round(k[i, j]), vtype=gurobipy.GRB.INTEGER, name=name)

  #修改机队信息
    # N[5] = 15
    # N[-1] = 15
    # 更新变量环境
    model.update()


    # 添加目标函数
    obj = gurobipy.LinExpr(0)
    for i in range(numbers_i):
        for j in range(numbers_j):
            obj.addTerms(-C_i_j[i, j], X[i, j])
        for m in range(11):
            obj.addTerms(p[i, m], Z_i_m[i, m])
    model.setObjective(obj, gurobipy.GRB.MAXIMIZE)


    # # 添加约束条件-1-航班机型覆盖
    for i in range(numbers_i):
        expr1 = gurobipy.LinExpr(0)
        for j in range(numbers_j):
            expr1.addTerms(1, X[i, j])
        model.addConstr(expr1 == 1, name='Constr_1' + str(i))


    # 约束条件-2飞机平衡约束
    for j in range(numbers_j):
        for m in flight_m:
            for k in m[1:-1]:
                expr1 = gurobipy.LinExpr(0)
                expr2 = gurobipy.LinExpr(0)
                for i in range(numbers_i):
                    expr1.addTerms(a_m_i[k, i], X[i, j])
                    expr2.addTerms(a_m_i[m[0], i], X[i, j])
                model.addConstr(expr1 == G_m_j[k, j] - G_m_j[k - 1, j], name='Constr_2_1' + str(k) + str(j))
                model.addConstr(expr2 == G_m_j[m[0], j] - G_m_j[m[-1], j], name='Constr_2_2' + str(k) + str(j))
                expr1.clear()
                expr2.clear()


    for index, m in enumerate(flight_m):
        for j in range(numbers_j):
            name = 'GE_' + str(index) + "_" + str(j)
            GE = model.addVar(lb=0, ub=1000, vtype=gurobipy.GRB.INTEGER, name=name)
            expr1 = gurobipy.LinExpr(0)
            expr1.addTerms(1, GE)
            model.addConstr(expr1 == G_m_j[m[-1], j])
            expr1.clear()


    #40分钟间隔约束
    M = 10000
    count = 0
    u = {}
    expr1_abs = {}
    for m, flight in zip(flight_m, airport_index):
        L = m[0:-1]
        for index, k in enumerate(L):
            if a_m_i[k + 1, flight[index + 1]] == -1 and a_m_i[k, flight[index]] == 1:
                for j in range(numbers_j):
                    expr1 = gurobipy.LinExpr(0)
                    expr2 = gurobipy.LinExpr(0)
                    expr1.addTerms(T_m_i[k + 1, flight[index + 1]] * a_m_i[k + 1, flight[index + 1]],
                                   X[flight[index + 1], j])
                    expr1.addTerms(T_m_i[k, flight[index]] * a_m_i[k, flight[index]], X[flight[index], j])
                u[count] = model.addVar(lb=0, ub=1, vtype=gurobipy.GRB.BINARY)
                expr1_abs[count] = model.addVar(lb=0, ub=5000, vtype=gurobipy.GRB.CONTINUOUS)
                model.addConstr(expr1 <= expr1_abs[count])
                model.addConstr(-expr1 <= expr1_abs[count])
                model.addConstr(expr1_abs[count] <= expr1 + M - M * u[count])
                model.addConstr(expr1_abs[count] <= -expr1 + u[count] * M)
                model.addGenConstrIndicator(G_m_j[k + 1, j], True, expr1_abs[count] >= 40)
                count += 1

    # 约束条件-3机队规模约束
    for j in range(numbers_j):
        expr1 = gurobipy.LinExpr(0)
        for i in flight_m_end:
            expr1.addTerms(1, G_m_j[i, j])
        model.addConstr(expr1 <= N[j], name='Constr_3' + str(j))

    # 约束条件-4飞机座位约束
    for i in range(numbers_i):
        expr1 = gurobipy.LinExpr(0)
        for j in range(numbers_j):
            expr1.addTerms(S[j], X[i, j])
        for m in range(11):
            expr1.addTerms(-1, Z_i_m[i, m])
        model.addConstr(expr1 >= 0, name='Constr_4' + str(i))
        expr1.clear()

    # 约束条件-5经停航班约束
    for j in range(numbers_j):
        for index, i in enumerate(flights):
            expr1 = gurobipy.LinExpr(0)
            for k in i:
                expr1.addTerms(1, X[k, j])
            expr1.addTerms(-len(i), y[j, index])
            model.addConstr(expr1 == 0, name='Constr_6' + str(j))
            expr1.clear()

    model.optimize()
    var_names = []
    var_values = []

    #储存解集合
    for var in model.getVars():
        var_names.append(str(var.varName))
        var_values.append(var.X)

    # Write to csv
    result = pd.DataFrame()
    result['feature'] = var_names
    result['label'] = var_values
    result.to_csv('model_out.csv')

    # # model.computeIIS()
    # # 打印每种机型的使用情况
    print_result()

    print('Obj:', model.objval)
    # # for v in model.getVars():
    # #
    # #     print(f"{v.varname}: {round(v.x, 2)}")
