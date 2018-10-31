from pyecharts import EffectScatter

es = EffectScatter("动态散点图各种图形演示")
es.add("pin",[10],[10],symbol_size=20,effect_scale=3.5,
       effect_period=3,symbol='pin')
es.add("rect", [20], [20], symbol_size=12, effect_scale=4.5,
       effect_period=4,symbol="rect")
es.add("roundRect", [30], [30], symbol_size=30, effect_scale=5.5,
       effect_period=5,symbol="roundRect")
es.add("diamond", [40], [40], symbol_size=10, effect_scale=6.5,
       effect_brushtype='fill',symbol="diamond")
es.add("arrow", [50], [50], symbol_size=16, effect_scale=5.5,
       effect_period=3,symbol="arrow")
es.add("triangle", [60], [60], symbol_size=6, effect_scale=2.5,
       effect_period=3,symbol="triangle",is_more_utils=True)
es.render(path="EffectScatter.html")