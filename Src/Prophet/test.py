import pandas as pd
from prophet import Prophet
df = pd.read_csv('example_wp_log_peyton_manning.csv')
df.head()