import plotly.graph_objects as go
data=[{"x": [1, 2, 3, 4, 5], "y": [6, 7, 8, 9, 10]},{"x":[6, 7, 8, 9, 10], 
"y": [1, 2, 3, 4, 5]}] 
fig = go.Figure() 
for i in range(len(data)): 
 fig.add_trace(go.Scatter(x=data[i]["x"], y=data[i]["y"], 
mode='lines+markers')) 
 fig.update_layout(title="SIDDHARTH OJI", xaxis_title="time", 
yaxis_title="value") 
fig.show() 
import pandas as pd
import plotly.graph_objects as go
dat=pd.read_csv("sales1.csv") 
fig=go.Figure() 
fig.update_layout(title="SIDDHARTH OJI", xaxis_title="order dates", 
yaxis_title="value") 
fig.add_trace(go.Scatter(x=dat.iloc[0:,0],y=dat.iloc[5:,5],mode="lines+markers
")) 
fig.add_trace(go.Scatter(x=dat.iloc[0:,0],y=dat.iloc[4:,4],mode="lines+markers
")) 
fig.update_layout(title="SIDDHARTH OJI", xaxis_title="order dates", 
yaxis_title="value") 
fig.show() 

#pip3 install plotly pandas
