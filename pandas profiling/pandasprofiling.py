import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('C:\\Coding\\machine learning\\CSV Files\\train.csv')
profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file("output.html")