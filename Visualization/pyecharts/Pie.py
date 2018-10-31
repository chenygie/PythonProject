from pyecharts import Pie

attr = ["Shirt","Cardigan","Chiffon shirt","Pants","High heels","sock"]
values1 = [11,12,13,10,10,10]
values2 = [19,21,32,20,20,33]
pie = Pie("Pie chart - Rose diagram example",title_pos='center',width=900)
pie.add("commodity A",attr,values1,center=[25,50],is_random=True,
        radius=[30,75],rosetype='radius',is_more_utils=True)
pie.add("commodity B",attr,values2,center=[75,50],is_random=True,is_legend_show=False,
        radius=[30,75],is_label_show=True)
pie.render(path="Pie.html")
