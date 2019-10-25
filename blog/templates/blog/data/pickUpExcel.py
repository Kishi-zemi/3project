import openpyxl
import pandas as pd
from pandas import DataFrame
import xlrd

book = openpyxl.load_workbook("H28.xlsx")
sheet = book['Sheet1']

list = []
i = 2

while True:
    cell = sheet.cell(row=i, column=8).value #1->事故内容 8->事故類型 9->甲_種類 12->乙_種類
    if cell is None:
        break
    elif not cell in list:
        list.append(cell)
    i += 1

for i in range(len(list)):
    print(list[i])
