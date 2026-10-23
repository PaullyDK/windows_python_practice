from zipfile import *
f = ZipFile("files.zip", 'r', ZIP_STORED)
names = f.namelist()
for name in names:
    print("File Name:", name)
    print("The content of this file is:")
    f1 = open(name, 'r')
    print(f1.read())
    print()