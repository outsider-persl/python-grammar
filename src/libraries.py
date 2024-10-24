import random  # 随机数生成
import statistics  # 统计函数
import math  # 数学函数
import datetime  # 日期和时间
import numpy as np  # 数组和数学运算
import pandas as pd  # 数据分析
import matplotlib.pyplot as plt  # 数据可视化
import requests  # HTTP 请求
import json  # JSON 处理

# 使用 statistics 库
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mean = statistics.mean(data)  # 平均值
median = statistics.median(data)  # 中位数
mode = statistics.mode(data)  # 众数
stddev = statistics.stdev(data)  # 标准差
print(mean, median, mode, stddev)

# 使用 random 库
random_numbers = list(range(1, 11))
random.shuffle(random_numbers)  # 打乱顺序
print(random_numbers)

# 使用 math 库
square_root = math.sqrt(16)  # 计算平方根
print(square_root)

# 使用 datetime 库
current_time = datetime.datetime.now()  # 获取当前时间
print(current_time)

# 使用 numpy 库
array = np.array([1, 2, 3, 4, 5])
mean_np = np.mean(array)  # NumPy 的平均值
print(mean_np)

# 使用 pandas 库
data_dict = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 30, 22]}
df = pd.DataFrame(data_dict)  # 创建 DataFrame
print(df)

# 使用 matplotlib 库
plt.plot(data)  # 绘制数据图
plt.title('Line Graph')
plt.show()

# 使用 requests 库
response = requests.get('https://api.github.com')  # 发送 GET 请求
print(response.json())  # 输出 JSON 响应

# 使用 json 库
json_data = json.dumps(data)  # 转换为 JSON 字符串
print(json_data)
