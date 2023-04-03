import openpyxl as xl
from openpyxl.styles import Font,Alignment
wb=xl.load_workbook("C://MyDataSets//list_to_excel.xlsx")
sh=wb.active
font=Font(bold=True,size=20)
algnmt=Alignment(horizontal='center')
sh['A1'].font=font
sh['A1'].alignment=algnmt

# rows=[['neel','manu','sai'],[1,2,3],[5,6,7],[9,8,1]]
# wb=Workbook()
# sh=wb.active
# for row in rows:
#     sh.append(row)
wb.save("C://MyDataSets//list_to_excel.xlsx")