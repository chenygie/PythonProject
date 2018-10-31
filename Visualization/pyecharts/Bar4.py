from pyecharts import Bar,Line
bar = Bar("Bar的第一个主标题","Bar的次标题")
bar.add("服饰",["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
        [5, 20, 36, 10, 75, 90],is_more_utils=True)
line = Line("Line的主标题图表","Line的副标题图表")
line.add("服饰",["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
         [5, 20, 36, 10, 75, 90],is_more_utils=True)
bar.render(path="bar4.html")
line.render(path="line4.html")