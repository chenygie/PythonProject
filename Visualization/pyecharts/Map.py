from pyecharts import Map
# value = [155, 10, 66, 78]
# attr = ["福建", "山东", "北京", "上海"]
# map  = Map("中国地图")
# map.add("test_map",attr,value,maptype = "china",is_more_utils=True)

# value = [20, 190, 253, 77, 65]
# attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
# map = Map("广东地图示例", width=1200, height=600)
# map.add("", attr, value, maptype='广东', is_visualmap=True, visual_text_color='#000')

value = [95.1, 23.2, 43.3, 66.4, 88.5]
attr= ["China", "Canada", "Brazil", "Russia", "United States"]
map = Map("世界地图示例", width=1200, height=600)
map.add("",attr,value,maptype="world",is_visualmap=True,visual_text_color="#000")

map.render(path="Map3.html")
