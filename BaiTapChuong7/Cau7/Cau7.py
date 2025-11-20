import xlsxwriter
from pathlib import Path

OUTPUT = Path(__file__).with_name("demo.xlsx")
LOGO = Path(__file__).with_name("logo_UEL.png")

workbook = xlsxwriter.Workbook(OUTPUT)
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 5)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 20)
worksheet.set_column('D:D', 15)
worksheet.set_column('E:E', 15)

bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'STT', bold)
worksheet.write('B1', 'MÃ SẢN PHẨM', bold)
worksheet.write('C1', 'TÊN SẢN PHẨM', bold)
worksheet.write('D1', 'SỐ LƯỢNG', bold)
worksheet.write('E1', 'ĐƠN GIÁ', bold)

worksheet.write('A2', 1)
worksheet.write('B2', 'SP1')
worksheet.write('C2', 'Coca')
worksheet.write('D2', 15)
worksheet.write('E2', 15000)

worksheet.write('A3', 2)
worksheet.write('B3', 'SP2')
worksheet.write('C3', 'Pepsi')
worksheet.write('D3', 20)
worksheet.write('E3', 18000)

if LOGO.exists():
    worksheet.insert_image('B5', LOGO)
else:
    print('Missing logo_UEL.png next to the script; demo.xlsx still created without image')

workbook.close()
