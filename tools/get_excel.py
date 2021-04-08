import xlrd
from xlutils.copy import copy

def get_excel(names,startNum,endNum):
    list_data = []
    url = 'D:/Users/dca/PycharmProjects/TestProjectJieKou/data/dataM.xls'
    excel_data = xlrd.open_workbook(url,formatting_info=True)
    # excel_names = excel_data.sheet_names()
    excel_name = excel_data.sheet_by_name(names)
    #获取单元格内容 cell(行，列)
    for i in range(startNum-1,endNum):
        dan = excel_name.cell(i,0).value
        dan1 = excel_name.cell(i,1).value
        list_data.append((dan,dan1))
    return list_data

def set_excel():
    list_data = []
    url = 'D:/Users/dca/PycharmProjects/TestProjectJieKou/data/dataM.xls'
    excel_data = xlrd.open_workbook(url,formatting_info=True)
    excel_name_new = copy(excel_data)
    new_excel_data = excel_name_new.get_sheet(0)
    return  excel_name_new,new_excel_data
    #获取单元格内容 cell(行，列)

if __name__ == '__main__':
    # get_excel("loginData")
    for i in get_excel("loginData",0,4):
        print(i,"getexcel")

    print(set_excel())