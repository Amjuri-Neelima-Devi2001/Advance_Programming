from openpyxl import Workbook
from openpyxl.chart import BarChart,LineChart,Reference
workbook=Workbook()
sheet=workbook.active
rows=[['neel','manu','sai'],[1,2,3],[5,6,7],[9,8,1]]
for row in rows:
    sheet.append(row)
chart=BarChart()
data=Reference(worksheet=sheet,min_row=1,max_row=4,min_col=1,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,'E2')
workbook.save("C://MyDataSets//Barchart.xlsx")