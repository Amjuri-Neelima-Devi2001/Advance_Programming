import openpyxl as xl
wb=xl.load_workbook("C://MyDataSets//list.xlsx")
l=[]
# l1=[]
sheet=wb.active
for i in range(1,5):
    l1=[]
    # l.clear()
    for j in range(1,4):
        l1.append(sheet.cell(i,j).value)
    l.append(l1)
    # l.clear()
print(l)

