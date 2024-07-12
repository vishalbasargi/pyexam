from bokeh.plotting import figure,curdoc,show
from bokeh.models import ColumnDataSource
import numpy as np
x=np.random.randn(100) 
y=np.random.randn(100) 
source=ColumnDataSource(data=dict(x=x,y=y)) 
plot=figure(title="",height=400,width=500) 
plot.line('x','y',source=source,color="blue",alpha=0.5,line_width=2,legend_lab
el="Y vs X") 
curdoc().add_root(plot) 
show(plot) 

#sudo apt update
#sudo apt install python3 python3-pip
#nano bokeh_plot.py


#bokeh serve --show bokeh_plot.py

