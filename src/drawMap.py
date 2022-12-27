import loadData
from pyecharts.charts import Timeline, Map
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from os.path import dirname, abspath

namemap = {'黑龙江': 'Heilongjiang', '吉林': 'Jilin', '辽宁': 'Liaoning',
           '北京': 'Beijing', '天津': 'Tianjing', '河北': 'Hebei',
           '山西': 'Shanxi', '内蒙古': 'Inner Mongolia', '上海': 'Shanghai',
           '江苏': 'Jiangsu', '山东': 'Shandong', '浙江': 'Zhejiang',
           '安徽': 'Anhui', '江西': 'Jiangxi', '福建': 'Fujian',
           '广东': 'Guangdong', '澳门': 'Macau', '台湾': 'Taiwan',
           '香港': 'Hong Kong', '西藏': 'Tibet', '广西': 'Guangxi',
           '海南': 'Hainan', '河南': 'Henan', '湖北': 'Hubei',
           '湖南': 'Hunan', '陕西': 'Shaanxi', '新疆': 'Xinjiang',
           '宁夏': 'Ningxia', '甘肃': 'Gansu', '青海': 'Qinghai',
           '重庆': 'Chongqing', '四川': 'Sichuan', '贵州': 'Guizhou',
           '云南': 'Yunnan'}

dataType = 'Confirmed'
# dataType = 'Deaths'
# dataType = 'Recovered'
dataMax = {'Confirmed': 1800, 'Deaths': 30, 'Recovered': 1800}


def map_visualmap() -> Timeline:
    
    allData = loadData.LoadData(dataType.lower())

    tline = Timeline(opts.InitOpts(
        page_title=dataType+" COVID-19 Cases in China",
        width="1440px", height="720px",
        theme=ThemeType.LIGHT
    ))
    # create a timeline of maps

    for j in range(0, len(allData[0]['number']), 1):
        lastCases = []
        
        for i in range(1, len(allData), 1):
            # find the provinces of China
            if allData[i]['province'] != '' and allData[i]['country'] == 'China':
                lastCase = allData[i]['number'][j]
                lastCases.append([allData[i]['province'], int(lastCase)])

        # create every single map
        c = (
            Map(opts.InitOpts(width="1440px", height="720px"))
            .add(
                series_name=dataType+" Cases",
                data_pair=lastCases,
                maptype="china",
                name_map=namemap,
                is_map_symbol_show=False
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title=dataType+" COVID-19 Cases in China",
                    pos_left="center",
                    title_textstyle_opts=opts.TextStyleOpts(
                        font_size=30
                    )
                ),
                visualmap_opts=opts.VisualMapOpts(
                    max_=dataMax[dataType],
                    range_color=["#50a3ba",
                                 "#eac763",
                                 "#d94e5d",
                                 "#893445"],
                    is_piecewise=False
                ),
                legend_opts=opts.LegendOpts(
                    is_show=False
                )
            )
        )
        tline.add(c, allData[0]['number'][j])
        tline.add_schema(
            play_interval=60,
            is_auto_play=True,
            is_loop_play=True,
            symbol=None
        )
    return tline


if __name__ == '__main__':
    path = dirname(dirname(abspath(__file__))) + '\\result\\map\\map-' + dataType.lower() + '.html'
    map_visualmap().render(path)
