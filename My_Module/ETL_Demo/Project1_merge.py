import pandas as pd
from functools import reduce
from sqlalchemy import create_engine
l=[]
db_connection_str='mysql+pymysql://neel:neelima2001@localhost/myhcl'
db_connection=create_engine(db_connection_str)
sheet_names=['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
for i in sheet_names:
    df=pd.read_excel("C://MyDataSets//project1.xlsx",sheet_name=i)
    l.append(df)
di= pd.read_excel("C://MyDataSets//project1.xlsx", sheet_name=sheet_names)
data=reduce(lambda left,right:pd.merge(left,right,on='Prod_id',how='inner'),l)
# print(l)
# print(data)
# data.to_excel("C://MyDataSets//project_excel.xlsx")
try:
    di.to_sql(name="mytable1",con=db_connection)
except Exception as e:
    print(e)
