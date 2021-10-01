import pandas as pd
import numpy as np
import urllib.request
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings(action='ignore')

web_path = urllib.request.urlopen("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
dataset = pd.read_csv(web_path)

df = pd.DataFrame(data=dataset)

col = df.keys()[4:]
df_india = df[df['Country/Region'] == 'India'].iloc[0][col]
df_us = df[df['Country/Region'] == 'US'][col].iloc[0][col]

plt.plot(df_india, color = 'g', label = 'India')
plt.plot(df_us, color = 'b', label = 'US')
plt.legend()
plt.savefig("graph.png")
plt.show()
