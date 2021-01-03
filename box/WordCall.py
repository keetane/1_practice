#!/usr/bin/env python

from docx import Document

# ドキュメントオブジェクト作成
# <class 'docx.document.Document'>
document = Document('word.docx')

# データの表示
for i in document.paragraphs:
  print(i.text)