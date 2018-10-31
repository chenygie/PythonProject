from pyecharts import Polar
import random
'''
极坐标 示例
'''

polar = Polar("极坐标系-散点图示例")
# data = [(i,random.randint(1,100)) for i in range(101)]
# polar.add("",data,boundary_gap=False,type='scatter',is_angleaxis_show=True,
#           area_color="#f23",is_splitline_show=False)
radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
polar.add("A",[1, 2, 3, 4, 3, 5, 1],radius_data=radius,
          type='barRadius',is_stack=True)
polar.add("B",[2, 4, 6, 1, 2, 3, 1],radius_data=radius,
          type="barRadius",is_stack=True)
polar.add("C",[1, 2, 3, 4, 1, 2, 5],radius_data=radius,
          type="barRadius",is_stack=True)

polar.render(path="Polar2.html")

