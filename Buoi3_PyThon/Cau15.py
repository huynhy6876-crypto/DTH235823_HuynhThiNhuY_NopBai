'''(a) range(5)
    Tạo dãy số từ 0 đến 4 (mặc định bắt đầu từ 0, bước nhảy là 1).
    Kết quả: [0, 1, 2, 3, 4]
(b) range(5, 10)
    Tạo dãy số từ 5 đến 9 (bắt đầu từ 5, kết thúc trước 10, bước nhảy là 1).
    Kết quả: [5, 6, 7, 8, 9]
(c) range(5, 20, 3)
    Tạo dãy số từ 5 đến 19, mỗi lần tăng 3.
    Kết quả: [5, 8, 11, 14, 17]
(d) range(20, 5, -1)
    Tạo dãy số từ 20 đến 6, mỗi lần giảm 1.
    Kết quả: [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
(e) range(20, 5, -3)
    Tạo dãy số từ 20 đến 8, mỗi lần giảm 3.
    Kết quả: [20, 17, 14, 11, 8]
(f) range(10, 5)
    Không có số nào vì bước nhảy mặc định là +1, nhưng bắt đầu lớn hơn kết thúc.
    Kết quả: []
(g) range(0)
    Không có số nào vì kết thúc là 0.
    Kết quả: []
(h) range(10, 101, 10)
    Tạo dãy số từ 10 đến 100, mỗi lần tăng 10.
    Kết quả: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
(i) range(10, -1, -1)
    Tạo dãy số từ 10 đến 0, mỗi lần giảm 1.
    Kết quả: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
(j) range(-3, 4)
    Tạo dãy số từ -3 đến 3, mỗi lần tăng 1.
    Kết quả: [-3, -2, -1, 0, 1, 2, 3]
(k) range(0, 10, 1)
    Tạo dãy số từ 0 đến 9, mỗi lần tăng 1.
    Kết quả: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Lưu ý:

range(start, stop, step) tạo ra các số bắt đầu từ start, kết thúc trước stop, mỗi lần nhảy step.
Nếu bước nhảy không phù hợp với hướng đi (ví dụ: bước dương mà start > stop), kết quả là rỗng.
Bạn có thể dùng list(range(...)) để xem kết quả cụ thể trong VS Code.'''