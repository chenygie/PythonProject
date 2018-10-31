import numpy as np
import pandas as pd
from pyecharts import Bar
title = 'bar chart'
index = pd.date_range('3/8/2018',periods=6,freq='M')
df1 = pd.DataFrame(np.random.randn(6),index=index)
df2 = pd.DataFrame(np.random.randn(6),index=index)

dtvalue1 = [i[0] for i in df1.values]
dtvalue2 = [i[0] for i in  df2.values]
_index = [i for i in df1.index.format()]
bar = Bar(title,"Profit and loss situation")
bar.add("profit",_index,dtvalue1,is_stack=True,is_more_utils=True)
bar.add("loss",_index,dtvalue2,is_stack=True,is_more_utils=True)
bar.render(path="Bar5.html")