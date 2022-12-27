import numpy as np
import pandas as pd
from os.path import dirname, abspath
import csv

# 从csv文件中读取数据
# dataType: one of (confirmed, deaths, recovered)


def LoadData(dataType):
    '''Load data from csv file and return a list of dict'''

    # 打开csv文件
    path = dirname(dirname(abspath(__file__))) + '\\res\\time_series_covid19_' + dataType + '_global.csv'
    with open(path, 'r') as f:
        allData = []
        reader = csv.reader(f)
        rawData = list(reader)
        allData = []

        # 格式化数据
        for i in rawData:
            rowInData = dict(country=i[1], province=i[0],
                             location=i[2:4], number=i[4:])
            allData.append(rowInData)

    print('Load data from csv file successfully.')
    return allData


if __name__ == '__main__':
    LoadData(dataType='confirmed')
