from pyecharts import Bar,Timeline
import random

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
bar_1 = Bar("2012年销量","数据纯属虚构")
bar_1.add("春季",attr,[random.randint(10,100) for _ in range(6)])
bar_1.add("夏季",attr,[random.randint(10,100) for _ in range(6)])
bar_1.add("秋季",attr,[random.randint(10,100) for _ in range(6)])
bar_1.add("冬季",attr,[random.randint(10,100) for _ in range(6)])

bar_2 = Bar("2013年销量","数据纯属虚构")
bar_2.add("春季",attr,[random.randint(10,100) for _ in range(6)])
bar_2.add("夏季",attr,[random.randint(10,100) for _ in range(6)])
bar_2.add("秋季",attr,[random.randint(10,100) for _ in range(6)])
bar_2.add("冬季",attr,[random.randint(10,100) for _ in range(6)])

bar_3 = Bar("2014年销量","数据纯属虚构")
bar_3.add("春季",attr,[random.randint(10,100) for _ in range(6)])
bar_3.add("夏季",attr,[random.randint(10,100) for _ in range(6)])
bar_3.add("秋季",attr,[random.randint(10,100) for _ in range(6)])
bar_3.add("冬季",attr,[random.randint(10,100) for _ in range(6)])

bar_4 = Bar("2015年销量","数据纯属虚构")
bar_4.add("春季",attr,[random.randint(10,100) for _ in range(6)])
bar_4.add("夏季",attr,[random.randint(10,100) for _ in range(6)])
bar_4.add("秋季",attr,[random.randint(10,100) for _ in range(6)])
bar_4.add("冬季",attr,[random.randint(10,100) for _ in range(6)])

bar_5 = Bar("2016年销量","数据纯属虚构")
bar_5.add("春季",attr,[random.randint(10,100) for _ in range(6)])
bar_5.add("夏季",attr,[random.randint(10,100) for _ in range(6)])
bar_5.add("秋季",attr,[random.randint(10,100) for _ in range(6)])
bar_5.add("冬季",attr,[random.randint(10,100) for _ in range(6)])

bar_6 = Bar("2017年销量","数据纯属虚构")
bar_6.add("春季",attr,[random.randint(10,100) for _ in range(6)])
bar_6.add("夏季",attr,[random.randint(10,100) for _ in range(6)])
bar_6.add("秋季",attr,[random.randint(10,100) for _ in range(6)])
bar_6.add("冬季",attr,[random.randint(10,100) for _ in range(6)],
          is_legend_show=True)

timeline = Timeline(is_auto_play=True,timeline_bottom=0)
timeline.add(bar_1,"2012年")
timeline.add(bar_2,"2013年")
timeline.add(bar_3,"2014年")
timeline.add(bar_4,"2015年")
timeline.add(bar_5,"2016年")
timeline.add(bar_6,"2017年")
timeline.render(path="Timeline.html")


