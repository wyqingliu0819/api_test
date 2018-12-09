import xlrd

#打开Excel（work_book）
excel = xlrd.open_workbook("../data/data.xlsx")

#指定工作表
sheet = excel.sheet_by_name("登录")
#sheet = excel.sheet_by_index(0)

print(sheet.nrows)  #有效数据行数
print(sheet.ncols)  #有效数据列数

# print(sheet.row_values(0))  #打印第一行的数据
# print(sheet.row_values(1))
#
# print(sheet.cell(0,0).value)

#打印注册模块的用例
sheet_reg = excel.sheet_by_name("注册")
for i in range(1, sheet_reg.nrows):
    print(sheet_reg.row_values(i))

