import pandas as pd
import csv 
import plotly.express as px
f = pd.read_csv("C:/Users/aryan/Desktop/coding/Coding (Phython)/data visualization")
mean = f.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()