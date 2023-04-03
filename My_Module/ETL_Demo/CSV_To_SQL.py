import pandas as pd
from sqlalchemy import create_engine

db_connection_str='mysql+pymysql://neel:neelima2001@localhost/myhcl'
db_connection=create_engine(db_connection_str)
df=pd.read_excel("C://MyDataSets//sample_pivot.xlsx",sheet_name="Sheet1",parse_dates=['Date'])
# task1=pd.crosstab(index=df['Region'],columns=df['Type'],values=df['Sales'],aggfunc='mean')
# task2=pd.crosstab([df.Region,df.Date.dt.quarter],df.Type,values=df.Sales,margins=True,aggfunc='sum')
# task3=pd.crosstab([df.Region,df.Date.dt.month],df.Type,values=df.Sales,margins=True,aggfunc='sum')
# task4=pd.crosstab([df.Region,df.Date.dt.year],df.Type,values=df.Sales,margins=True,aggfunc='sum')
df.fillna('mean',inplace=True)
print(df.isna().sum())
print(df.sort_values(['Region',]))
print(df)
# try:
#     df.to_sql(name="mytable",con=db_connection)
# except Exception as e:
#     print(e)