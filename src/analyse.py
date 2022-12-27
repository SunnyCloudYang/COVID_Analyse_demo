import loadData
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from os.path import dirname, abspath


allData = loadData.LoadData(dataType='confirmed')
datecnt = len(allData[0]['number'])

# sigmoid function
def sigmoid(x, a, b, c, d):
    return a / (1 + np.exp(-b * (x - c))) + d

# 获取某个省份的数据
def getProvinceData(province, country):
    for i in range(1, len(allData), 1):
        if allData[i]['province'] == province and allData[i]['country'] == country:
            return allData[i]['number']
    print('No such province.')
    return None

# 获取某个国家的数据
def getCountryData(country):
    total = []
    for i in range(1, len(allData), 1):
        if allData[i]['country'] == country:
            total = [int(total[j]) + int(allData[i]['number'][j]) for j in range(datecnt)] if len(total) != 0 else allData[i]['number']
    return total if len(total) != 0 else None

# 多项式拟合
def analyse(type, location):
    # define x and y
    x = range(datecnt)
    y = getProvinceData(
        location[0], location[1]) if type == 'province' else getCountryData(location)

    if y == None:
        print('No such data.')
        return

    # transform y from string list to int list
    for i in range(len(y)):
        y[i] = int(y[i])

    x = np.array(x)
    y = np.array(y)

    # fit the data with polynomial regression
    degree = 5
    pred_y1 = np.polyval(np.polyfit(x, y, degree), x)
    print(np.poly1d(np.polyfit(x, y, degree)))
    print("r^2={:.4f}".format(r2_score(y, pred_y1)))  # print the regression function and r^2

    # fit the data with sigmoid function
    popt, pcov=curve_fit(sigmoid,x,y, p0=[max(y), 1, 1, 0], maxfev=10000)
    pred_y2 = sigmoid(x, popt[0], popt[1], popt[2], popt[3])
    print(popt)
    print("r^2={:.4f}".format(r2_score(y, pred_y2)))

    # draw the chart
    # draw the data points
    plt.plot(x, y,
             marker='o', markersize=3, 
             linewidth=2.0, color='red', 
             label='Data', zorder=0) 
    # draw the regression line1
    plt.plot(x, pred_y1, 
             linewidth=2.0, color='blue', 
             label='Polynomial Regression', zorder=1)
    # draw the regression line2
    plt.plot(x, pred_y2, 
             linewidth=2.0, color='green',
             label='Sigmoid Regression', zorder=2)

    plt.title('Covid-19 Confirmed Cases in ' + location if type ==
              'country' else location[0]+'-'+location[1])  # set the title of the chart
    plt.legend()
    
    # change x-axis to date, 7 days per label, only show month and day
    date = [allData[0]['number'][i]
            [:len(allData[0]['number'][i])-3] for i in range(datecnt)]
    plt.xticks(x[::7], date[::7], rotation=45)

    # set the label of x-axis and y-axis
    plt.xlabel('date')
    plt.ylabel('cases')

    path = dirname(dirname(abspath(__file__))) + '\\result\\fit\\fit_' + (location if type == 'country' else location[0]+'-'+location[1])
    # set width and height of the chart
    plt.rcParams['figure.figsize'] = (14.40, 7.20)
    plt.savefig(
        path + '.png',
        dpi=256,
        bbox_inches='tight')
    plt.clf()
    
    with open(path + '.txt', 'a') as f:
        f.truncate(0)
        f.write('Polynomial Regression: \n' + str(np.poly1d(np.polyfit(x, y, degree))))
        f.write("\nr^2={:.4f}\n".format(r2_score(y, pred_y1)))
        f.write('\nSigmoid Regression: \n' + str(popt) + "\nr^2={:.4f}\n".format(r2_score(y, pred_y2)))


analyse('province', ['Hubei', 'China'])
# analyse('country', 'US')
