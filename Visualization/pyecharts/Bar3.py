from pyecharts import Bar

CLOTHES = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
clothes_v1 = [5, 20, 36, 10, 75, 90]
clothes_v2 = [10, 25, 8, 60, 20, 80]

bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", CLOTHES, clothes_v1, is_stack=True,is_more_utils=True)
bar.add("商家B", CLOTHES, clothes_v2, is_stack=True,is_more_utils=True)
bar.render(path="bar_Stack_3.html")
