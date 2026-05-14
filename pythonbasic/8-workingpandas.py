import pandas as pd
df = pd.read_csv('util/dataset/nyc_weather.csv')
# print(df['EST'][1])
# print(df[['EST', 'Temperature']])
# print(df['EST'],[df['Events'] == 'Rain'])
# add new field runtime
# df['runtime'] = df['Temperature'] + 10
# print(df['runtime'][0])
# df.fillna(0, inplace=True)
print(df['WindSpeedMPH'].mean())
# print(df['WindSpeedMPH'].max())
