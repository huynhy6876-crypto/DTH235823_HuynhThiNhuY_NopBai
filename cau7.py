#Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python.
"""1. Các loại lỗi trong Python
a) Lỗi cú pháp (Syntax Error)

Xảy ra khi viết sai quy tắc ngữ pháp Python.

Trình thông dịch phát hiện ngay và không chạy chương trình.

print("Hello"  # quên dấu đóng ngoặc


 Thông báo: SyntaxError: unexpected EOF while parsing

b) Lỗi thời gian chạy (Runtime Error / Exception)

Xảy ra khi chương trình đang chạy do dữ liệu hoặc thao tác không hợp lệ.

Ví dụ: chia cho 0, truy cập phần tử không tồn tại, ép kiểu sai.

x = 5 / 0       # ZeroDivisionError
y = int("abc")  # ValueError
a = [1, 2]
print(a[5])     # IndexError

c) Lỗi logic (Logic Error)

Chương trình chạy không báo lỗi, nhưng kết quả sai so với mong đợi.

Khó phát hiện hơn vì không có thông báo lỗi.

# Tính trung bình nhưng quên chia
numbers = [2, 4, 6]
avg = sum(numbers)  # lỗi logic: thiếu / len(numbers)
print(avg)  # In ra 12 thay vì 4

 2. Cách bắt lỗi trong Python

Python cung cấp cơ chế xử lý ngoại lệ (Exception Handling) bằng khối try ... except ....

a) Cấu trúc cơ bản
try:
    # đoạn code có thể gây lỗi
    x = int("abc")
except ValueError:
    # xử lý khi có lỗi
    print("Không thể chuyển đổi sang số nguyên")

b) Bắt nhiều loại lỗi
try:
    a = [1, 2]
    print(a[5])
except ValueError:
    print("Lỗi giá trị")
except IndexError:
    print("Lỗi chỉ số mảng")

c) Bắt tất cả lỗi
try:
    x = 10 / 0
except Exception as e:
    print("Có lỗi xảy ra:", e)

d) Sử dụng else và finally

else: chạy khi không có lỗi.

finally: chạy luôn luôn, dù có lỗi hay không (thường dùng để giải phóng tài nguyên).

try:
    x = int(input("Nhập số: "))
except ValueError:
    print("Sai định dạng số!")
else:
    print("Bạn nhập:", x)
finally:
    print("Kết thúc chương trình")
"""