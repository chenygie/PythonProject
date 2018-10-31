from pyecharts import Radar

schema = [
    ("销售", 6500), ("管理", 16000), ("信息技术", 30000),
    ("客服", 38000), ("研发", 52000), ("市场", 25000)
]

v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]

radar = Radar()
radar.config(schema,shape="circle")
radar.add("预算分配",v1,is_splitline_show=True,is_axisline_show=True,
          is_stack=True)
radar.add("实际开销",v2,label_color=["#23e"],is_area_show=False,is_stack=True)

# radar.add("实际开销",v2,label_color=["#23e"],is_area_show=False,
#           legend_selectedmode='single',is_stack=True)

radar.render(path="Radar.html")