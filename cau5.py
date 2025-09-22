
"""1. Toán tử số học
/ (chia thực)

Luôn trả về số thực (float), kể cả khi chia hết.

5 / 2   # 2.5
10 / 5  # 2.0

// (chia lấy phần nguyên – floor division)

Trả về phần nguyên của phép chia.

Với số âm, kết quả được làm tròn xuống (floor).

5 // 2    # 2
-5 // 2   # -3 (làm tròn xuống)

% (chia lấy dư – modulo)

Trả về phần dư của phép chia.

5 % 2    # 1
10 % 3   # 1
-5 % 2   # 1  (quy tắc: (a // b)*b + (a % b) = a)

** (lũy thừa – exponentiation)

Dùng để tính số mũ.

2 ** 3   # 8
5 ** 0.5 # 2.236... (căn bậc hai của 5)

 2. Toán tử logic
and

Trả về True nếu cả hai toán hạng đều đúng.

True and True   # True
True and False  # False

or

Trả về True nếu ít nhất một toán hạng đúng.

True or False   # True
False or False  # False


 Lưu ý: and và or trong Python không chỉ trả về True/False mà còn có thể trả về toán hạng cuối cùng được đánh giá:

5 and 10   # 10 (cả 5 và 10 đều True → trả về 10)
0 or 7     # 7  (0 là False, nên lấy 7)

 3. Toán tử so sánh định danh
is

Dùng để so sánh địa chỉ ô nhớ (identity) của hai đối tượng, không phải giá trị.

Trả về True nếu cả hai biến cùng tham chiếu đến một đối tượng trong bộ nhớ.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True (b tham chiếu cùng chỗ nhớ với a)
print(a is c)  # False (giá trị bằng nhau, nhưng khác ô nhớ)
print(a == c)  # True  (so sánh giá trị)
"""