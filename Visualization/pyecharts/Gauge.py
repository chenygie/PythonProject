from pyecharts import Gauge

gaue = Gauge("仪表盘示例")
gaue.add("业务指标","完成指标",66.66,is_more_utils=True)
gaue.render(path="gaue.html")