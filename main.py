import pandas as pd
# import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import requests
import numpy as np
import bs4
import time

pytrend = TrendReq(hl='en-US', tz=360, retries=10, backoff_factor=0.5)


pd.set_option("display.max_rows", None, "display.max_columns", None)

country_code_data = pd.read_csv("country-codes.csv")
country_code_data = country_code_data.dropna(subset=['official_name_en'])
countries = country_code_data[["official_name_en", "ISO3166-1-Alpha-3", "ISO3166-1-Alpha-2"]]

kw_list = ['corona', 'coronavirus']
lis = countries.index[194:]
for ind in lis:
    print(ind)
    #if (ind>=152):
    time.sleep(5)
    pytrend.build_payload(
        kw_list=kw_list,
        geo=countries["ISO3166-1-Alpha-2"][ind],
        timeframe='2020-02-01 2020-10-06',
    )
    df_time = pytrend.interest_over_time()
    df_time = df_time.loc[:, df_time.columns != 'isPartial']
    df_time["country_code"] = countries["ISO3166-1-Alpha-3"][ind]
    df_time['country_name'] = countries["official_name_en"][ind]

    # df_region= pytrend.interest_by_region()
    #print(df_time)
    df_time.to_csv('google_trends_data.csv', mode='a', header=True)