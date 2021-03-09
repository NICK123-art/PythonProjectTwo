import PyPDF2
import openpyxl

fn = 'sales_001.xlsx'
wb = openpyxl.load_workbook(fn, data_only=True)
ws = wb.get_sheet_by_name('全国订单明细')
for cell in list(ws.columns)[0]:
    print(cell.value)
for cell in list(ws.rows)[1]:
    print(cell.value,end = ' ')
