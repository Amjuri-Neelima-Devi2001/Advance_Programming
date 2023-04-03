import openpyxl as xl
from openpyxl import Workbook
rows=[['neel','manu','sai'],[1,2,3],[5,6,7],[9,8,1]]
wb=Workbook()
sh=wb.active
for row in rows:
    sh.append(row)
wb.save("C://MyDataSets//list_to_excel.xlsx")