#!/usr/bin/env python

from docx import Document

# ファイル名
word_read_file_name = "word.docx"

# ドキュメントオブジェクト作成
# <class 'docx.document.Document'>
document = Document(word_read_file_name)

# データの表示
for i in document.paragraphs:
  print(i.text)