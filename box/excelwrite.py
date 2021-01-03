#!/usr/bin/env python

from openpyxl import Workbook

# ファイル名
excel_write_file_name = "kuku.xlsx"

# シート名
sheet_name = "kuku"

# ワークブックオブジェクトの作成
# <class 'openpyxl.workbook.workbook.Workbook'>
wb = Workbook()

# ワークシートオブジェクトの作成
# <class 'openpyxl.worksheet.worksheet.Worksheet'>
sheet = wb.active

# シート名変更
sheet.title = sheet_name

# シート選択
ws = wb[sheet_name]

# 九九をワークシートオブジェクトに書き込み
for i in range(1, 10):
  for j in range(1, 10):
    sheet.cell(row=i, column=j, value=i * j)

# excel ファイルに書き込み
wb.save(excel_write_file_name)