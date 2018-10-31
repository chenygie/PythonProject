from pyecharts import HeatMap
import numpy
x_axis = ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
          "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
y_aixs = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]

data = [[i,j,numpy.random.randint(0,15)] for i in range(24) for j in range(7)]
heatmap = HeatMap()
heatmap.add("热力图直角坐标系",x_axis,y_aixs,data,is_visualmap=True,
            visual_text_color="#000",visual_orient="horizontal",
            is_more_utils=True)
heatmap.render(path="heatmap.html")