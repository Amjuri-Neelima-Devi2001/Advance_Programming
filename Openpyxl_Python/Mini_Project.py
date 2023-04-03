import pandas as pd
# from openpyxl import Workbook
import openpyxl
df=pd.read_excel("C://MyDataSets//master_data.xlsx")
# df1=pd.read_excel("C://MyDataSets//daily_data.xlsx")
# wb=Workbook()
# sheet=wb.active
def main(sheet_name):
    rows_count=1
    blank=0
    for i in range(2,len(df.index)+1):

print(main(master_data))
