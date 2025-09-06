import sys

# Kiểm tra xem có tham số dòng lệnh hay không
if len(sys.argv) > 1:
    # Nối các tham số thành một chuỗi
    chuoi = " ".join(sys.argv[1:])
    print("Chuỗi nhập vào là:", chuoi)
else:
    print("Vui lòng nhập chuỗi ở tham số dòng lệnh.")