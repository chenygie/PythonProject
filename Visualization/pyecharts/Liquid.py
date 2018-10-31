from pyecharts import Liquid

liquid = Liquid("水球图示例")
data = [0.6, 0.5, 0.4, 0.3]
liquid.add("test_Liquid",data,is_liquid_outline_show=False)
liquid.render(path="Liquid.html")