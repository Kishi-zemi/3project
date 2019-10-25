import xlrd
import pandas as pd
from pandas import DataFrame

def readExcel(fileName):
    book = xlrd.open_workbook(fileName)
    sheet = book.sheet_by_index(0)
    read_list = []
    for row_index in range(sheet.nrows):
        read_list.append(sheet.row_values(row_index))
    return read_list

def saveCSV(save_list, fileName, head):
    if len(save_list) == 0:
        save_list.append("None")
    DataFrame(save_list).to_csv(fileName, header = head, index = None)

reader = readExcel("H28.xlsx")

saveCSV(reader, "H28.csv", head = None)
