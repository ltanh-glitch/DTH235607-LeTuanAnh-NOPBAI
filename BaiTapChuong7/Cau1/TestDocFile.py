from XuLiFile import *
dssp = DocFile('database.txt')
def XuatSanPham (dssp):
    for row in dssp:
        for element in row:
            print(element, end = '\t')
        print()
    print()
XuatSanPham(dssp)
def SortSp(dssp):
    for i in range (len(dssp)):
        for j in range (len(dssp)):
            a = dssp[i]
            b = dssp[j]
            if (a[2] > b[2]):
                dssp[i] = b
                dssp[j] = a
SortSp(dssp)
print("Sản phẩm sau khi sắp xếp giá: ")
XuatSanPham(dssp)