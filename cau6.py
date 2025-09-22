#Trình bày một số cách nhập dữ liệu từ bàn phím
"""Trong Python, để nhập dữ liệu từ bàn phím ta thường dùng hàm input(). Dưới đây là một số cách phổ biến:

 1. Nhập chuỗi (mặc định input() trả về str)
name = input("Nhập tên của bạn: ")
print("Xin chào,", name)


 Ví dụ nhập Nam → in ra Xin chào, Nam

 2. Nhập số nguyên (int)

Cần ép kiểu bằng int().

age = int(input("Nhập tuổi của bạn: "))
print("Năm sau bạn sẽ:", age + 1)

 3. Nhập số thực (float)

Cần ép kiểu bằng float().

height = float(input("Nhập chiều cao (m): "))
print("Chiều cao của bạn là:", height, "m")

 4. Nhập nhiều giá trị trên một dòng

Dùng split() để tách theo khoảng trắng, sau đó ép kiểu nếu cần.

a, b = input("Nhập hai số: ").split()
print("a =", a, "b =", b)


 Ví dụ nhập: 5 7 → in ra a = 5 b = 7

Ép kiểu số nguyên:

a, b = map(int, input("Nhập hai số nguyên: ").split())
print("Tổng =", a + b)

 5. Nhập danh sách nhiều phần tử
numbers = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))
print("Danh sách:", numbers)


 Ví dụ nhập: 1 2 3 4 5 → in ra [1, 2, 3, 4, 5]

 6. Nhập nhiều dòng liên tiếp (dùng vòng lặp)
n = int(input("Nhập số lượng phần tử: "))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(x)

print("Danh sách:", arr)
"""