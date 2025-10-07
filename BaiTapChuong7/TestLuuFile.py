from XuLiFile import *
masp = input('Nhập mã sản phẩm: ')
tensp = input('Nhập tên sản phẩm: ')
dongia = input('Nhập đơn giá: ')
line = masp + ';' + tensp + ';' + dongia

LuuFile ('database.txt' , line)