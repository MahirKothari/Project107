import pandas  as pd 
import plotly.express as px
import csv
import plotly.graph_objects as go
df = pd.read_csv('pixelMathData.csv')
print(df.groupby(['student_id','level'],as_index = False)['attempt'].mean())
mean = df.groupby(['student_id','level'],as_index = False)['attempt'].mean()
#fig = go.Figure(go.Bar(x = mean,y = ['Level1','Level2','Level3','Level4'],orientation = 'h'))
fig = px.scatter(mean,x = 'student_id', y = 'level',size = 'attempt', color = 'attempt')
fig.show()