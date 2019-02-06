from adverity_neuses.meta import DebugMeta
from pytrends.request import TrendReq
from adverity_neuses.helpers import xprint, CalculateSMA
from datetime import datetime, timedelta
import pandas as pd
import json
import sys
import numpy as np
import os
from operator import itemgetter
from functools import partial

WORKING_DIR = os.getcwd()

class ContentManager(metaclass=DebugMeta):

    def __init__(self):
        pass



    @staticmethod
    #@lru_cache(1)  # your cache could be here
    def buildTask1Content():
        """
        This function is static because in a realworld application we could then put the result of it in a cache
        :return: Content for View
        """

        content = {}

        #reading the csv file
        chunks = pd.read_csv(WORKING_DIR + '\\train.csv',
                             chunksize=1000000,
                             sep=',',
                             usecols=[1, 2],
                             #nrows=10000000            #this allows a partial read of the csv
                             )
        
        df = pd.DataFrame()
        df = pd.concat(chunk for chunk in chunks)
        """

        ## This is my debugging dataframe which is much smaller and does not overheat my laptop :)
        click = [0,1,0,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0]
        hour = ['14082500', '14082500','14082501','14082400','14082400','14082400','14082401','14082401','14082401',
                '14082409','14082409','14082409','14082409','14082409','14082417','14082417','14082417','14082417']
        xprint(len(click))
        xprint(len(hour))
        df = pd.DataFrame({'click': click, 'hour': hour})
        """

        df['hour'] = pd.to_datetime(df['hour'], format='%y%m%d%H', errors='ignore')
        xprint("Finished Reading CSV File.")

        #aggregating iteratively to the hour level
        aggregated_df = df.groupby([df['hour'].dt.year, df['hour'].dt.month,df['hour'].dt.day, df['hour'].dt.hour]).sum()

        yAxisData = aggregated_df['click'].values.tolist()
        xAxisData = aggregated_df['click'].keys().tolist()
        xAxisData=[datetime(raw_datetime[0],
                  raw_datetime[1],
                  raw_datetime[2],
                  raw_datetime[3],
                  0).strftime("%Y-%m-%d %H:%M") for raw_datetime in xAxisData]

        # content dict is afterwards dumped into json format (view.py)
        content['YAxisData'] = yAxisData
        content['XAxisData'] = xAxisData

        #Calculating a simple Moving Average (every value has the same weight, n= Number of Values)
        simple_moving_average = CalculateSMA(n=12,timestamps=xAxisData,values=yAxisData)

        # calculates the sample standard dev under the assumption that the sample is just a
        #  small share of the population and the "true", hidden deviation must be extrapolated
        # ddof=0 enables Population standard deviation
        sample_standard_deviation = np.std([e[1] for e in simple_moving_average], ddof=1)

        offset = sample_standard_deviation*1.5
        content['SMA'] = simple_moving_average
        content['SMAUpperBand'] = [[e[0], e[1]+ offset] for e in simple_moving_average]
        content['SMALowerBand'] = [[e[0], e[1]- offset] for e in simple_moving_average]

        return content


    @staticmethod
    #@lru_cache(1)  # your cache could be here
    def buildTask2Content(keywords=""):
        """
        This function is static because in a realworld application we could then put the result of it in a cache
        :return: Content for View
        """
        content = {}
        keyword_list=keywords.split(",") if keywords!="" else ['']

        #setting up the api handler
        pytrend = TrendReq(hl='en-US', tz=360)

        # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
        pytrend.build_payload(keyword_list, cat=0, timeframe='today 5-y', geo='', gprop='')

        # Interest Over Time, getting data and organizing it in dataframe
        interest_over_time_df = pytrend.interest_over_time()

        interest_over_time_df['index_col'] = interest_over_time_df.index
        xAxisData = []
        xAxis_Timestamps = interest_over_time_df[keyword_list[0]].index.tolist()

        #improving date format
        for timestamp in xAxis_Timestamps:
            xAxisData.append(timestamp.strftime('%Y-%m-%d'))

        yAxisData=[]
        for idx,kw in enumerate(keyword_list):
            yAxisData.append(interest_over_time_df[kw].values.tolist())

        #content is afterwards dumped into json format (view.py)
        content['XAxisData'] = xAxisData
        content['YAxisData'] = yAxisData
        content['Keywords'] =  keyword_list

        return content
