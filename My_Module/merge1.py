import pandas as pd
sheet1=pd.read_excel("C://MyDataSets//Arrival_Dates.xlsx")
sheet2=pd.read_excel("C://MyDataSets//Arrival_Dates_Final.xlsx")
# df_sheet=sheet1.compare(sheet2,keep_equal=True)
df_sheet1=sheet1.compare(sheet2,align_axis=1)
# print(df_sheet)
print(df_sheet1)