import pandas as pd
import wbdata
import numpy
import datetime
import LinearRegression
wbdata.get_source()
wbdata.get_indicator(source=1)
#get country codes with a search
wbdata.search_countries('Poland')
#get indicators with a search
wbdata.search_indicators('population, total')
wbdata.get_data('SP.POP.TOTL', country='NOR')                                   #takes the value population total for Norway
wbdata.search_indicators('GDP')
wbdata.get_data('NY.GDP.MKTP.CD', country='NOR')                                #takes the GDP for Norway

a = pd.DataFrame.from_dict(wbdata.get_data('SP.POP.TOTL', country='NOR'))
a[['value','date']]
b=pd.DataFrame.from_dict(wbdata.get_data('NY.GDP.MKTP.CD',country='NOR'))
b[['value','date']]

data_date = (datetime.datetime(1990, 1, 1), datetime.datetime(2018, 1, 1))
indicators = {"SP.POP.TOTL": "Total Population","NY.GDP.MKTP.CD": "GDP"}
df = wbdata.get_dataframe(indicators,country=["NOR"],convert_date=True)

