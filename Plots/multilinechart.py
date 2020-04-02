import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV File
df = pd.read_csv('..\Datasets\Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

# Prep Data
trace1 = go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='Actual Max')
trace2 = go.Scatter(x=df['date'], y=df['actual_min_temp'], mode='lines', name='Min')
trace3 = go.Scatter(x=df['date'], y=df['actual_mean_temp'], mode='lines', name='Mean')
data = [trace1, trace2, trace3]

# Prep layout
layout = go.Layout(title="Temps", xaxis_title="Date", yaxis_title="Temps")

#Plot it and save html
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='tempmultiline.html')