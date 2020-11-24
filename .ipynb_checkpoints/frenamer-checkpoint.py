import glob
import os

path = "./test/"
files = os.listdir(path) # file = glob.glob(path + "*")と同じ
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
# file名のみの一覧を取得したい場合は、同じように、os.path.isfile()を使う。
kw = input("Enter the filename ")

for i, f in enumerate(files_dir):
    dname = kw + "{0:03d}".format(i)
    os.rename(path + f, path + dname)