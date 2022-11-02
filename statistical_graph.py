# -*- coding: utf-8 -*-

"""
画统计图：折线图 plot，饼图 pie，柱状图 bar

"""

import matplotlib.pyplot as plt
import numpy as np

# # 折线图 plot
# # 折线图数据
# date = ['1.28', '1.29', '1.30', '1.31', '2.1', '2.2']
# new_confirmed_cases = [1771, 1989, 2891, 2231, 3122, 1232]
# new_suspected_cases = [2351, 2798, 3769, 2633, 4507, 1367]
#
# # 画折线图
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 必须要写才能显示中文！！！ 设置字体为黑体
# plt.title('每日确诊人数和疑似病例')
# plt.plot(date, new_confirmed_cases, 'ro-', label='新增确诊病例')  # r红，o点，-线
# plt.plot(date, new_suspected_cases, 'bo-', label='新增疑似病例')
# plt.xlabel('日期')
# plt.ylabel('人数')
# plt.legend()  # 显示图例
# plt.show()  # 显示整个图表


# # 饼图 pie
# city = ['杭州', '丽水', '温州', '宁波', '金华']
# confirmed_cases = [100, 200, 400, 200, 50]
# el = [0, 0, 0.05, 0, 0.1]
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 必须要写才能显示中文！！！ 设置字体为黑体
# plt.title('浙江各地确诊人数占比')
# plt.pie(confirmed_cases, labels=city, autopct='%.2f%%', explode=el, shadow=True) # 数据autopct显示格式，explode偏移量，shadow阴影
# plt.show()


# 柱状图 bar
city = ['杭州', '丽水', '温州', '宁波', '金华']
confirmed_cases = [100, 200, 400, 200, 50]
cured_cases = [80, 30, 60, 20, 10]

plt.rcParams['font.sans-serif'] = ['SimHei']  # 必须要写才能显示中文！！！ 设置字体为黑体
plt.title('浙江各地的确诊人数与治愈人数对比')

# 画柱子
bar_width = 0.4
plt.bar(range(len(city)), confirmed_cases, color='blue', width=bar_width,
        label='确诊人数')  # range(len(city)，获取坐标[0,1,2,3,4]
plt.bar(np.arange(len(city)) + bar_width + 0.005, cured_cases, color='red', width=bar_width,
        label='治愈人数')  # np.arange(len(city))+bar_width+0.005，np.l获取list，并将arange(len(city))里的每一个坐标都+bar_width+0.005
# 在每个柱子上加数据文本
for x, y in enumerate(confirmed_cases):  # enumerate(p)返回p里每个值的index和value
    plt.text(x, y + 5, str(y), ha='center', va='bottom')
for x, y in enumerate(cured_cases):
    plt.text(x + bar_width + 0.005, y + 5, str(y), ha='center', va='bottom')
# 在每两个柱底中间加标签 （默认为在每个标准柱中间标坐标0，1，2，3，4）
plt.xticks(np.arange(len(city)) + (bar_width + 0.005) / 2, city)

plt.legend()
plt.show()
