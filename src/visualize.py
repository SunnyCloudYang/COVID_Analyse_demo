import loadData
from pyecharts.charts import Line
from pyecharts import options as opts
from os.path import dirname, abspath

allData = loadData.LoadData(dataType='confirmed')
# dataType: one of (confirmed, deaths, recovered)

line = Line(init_opts=opts.InitOpts(width="1440px", height="720px"))
# the width and height of the chart

x = allData[0]['number']  # x-axis is the date
line.add_xaxis(xaxis_data=x)

# y-axis is the number of confirmed cases
for i in range(1, len(allData), 1):  # find the provinces of China
    if allData[i]['province'] != '' and allData[i]['country'] == 'China':
        line.add_yaxis(
            series_name=allData[i]['province'],
            y_axis=allData[i]['number'],
            is_selected=(False if allData[i]['province'] == 'Hubei' else True)
        )
        # Hubei's confirmed cases is too large to show in the chart, so it is not selected by default, you can click the legend to show it

line.set_global_opts(
    title_opts=opts.TitleOpts(
        title="Covid-19 Confirmed Cases in China",
        pos_left="center",
        title_textstyle_opts=opts.TextStyleOpts(font_size=25),
    ),  # style of the title
    legend_opts=opts.LegendOpts(
        pos_right="left",
        orient="vertical",
        pos_top="middle",
        item_height=12,
        item_gap=8
    )  # style of the legend
)
line.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# hide the label of each point, or it will cover the line

path = dirname(dirname(abspath(__file__))) + '\\result\\visual\\visualize.html'
line.render(path=path)
# save the chart as a html file
