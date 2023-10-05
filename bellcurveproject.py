import plotly.figure_factory as px
import csv
import pandas as pd

df = pd.read_csv("data.csv")
fig = px.create_distplot([df["Avg Rating"]. to_list()], ["Avg Rating"])
fig.show()

