from pyecharts import Bar,Line,Overlap

attr = ['A','B','C','D','E','F']
values1 = [10,20,30,40,50,60]
values2 = [38,28,58,48,78,68]
bar = Bar("Bar-Line 示例")
bar.add("bar",attr,values1,is_more_utils=True,
        mark_point=['max','min'],mark_line=['average'])
line = Line()
line.add("line",attr,values2,is_more_utils=True,
         mark_point=['max','min'],mark_line=['average'])

overlap = Overlap()
overlap.add(bar)
overlap.add(line)
overlap.render(path="overlap.html")