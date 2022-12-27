res 文件夹下是数据文件，就是那3个csv文件

result 文件夹下是生成的网页和拟合结果
  |----fit 文件夹是回归分析结果，分析中加入了sigmoid函数，对于只有一波疫情的地方拟合效果很好，有两波疫情的地方多项式回归效果更好
  |----map 文件夹下是国内各地病例数量随时间变化的可视化演示
  |----visual 文件夹下是国内病例数量变化的折线图

src 文件夹下是源代码文件
  |----loadData.py：从csv文件中读取数据
  |----analyse.py：对某国或者某省数据进行回归拟合，会在\result\fit\下生成一个png图片和一个txt，txt里是拟合得到的多项式和sigmoid函数参数
  |----drawMap.py：对疫情病例数进行地图可视化
  |----visualize.py：在\result\visual\下生成折线图，目前还不能生成国外疫情数据折线图，想生成的话改一下for循环就可以


其他文件都不重要，可以删除也可以留着。
代码放在了GitHub上，有更新（估计不太会有了）去那上面下最新的zip然后解压就行，这是网址：https://github.com/SunnyCloudYang/COVID_Analyse_demo