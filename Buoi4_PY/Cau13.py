# Câu 13: Hàm kiểm tra số hoàn thiện, số thịnh vượng
# Yêu cầu:
# Viết hàm tính tổng ước số để áp dụng chung cho 2 bài dưới đây:
# a) Kiểm tra số nguyên dương n có phải là số hoàn thiện (Pefect number) hay không?
# (Số hoàn thiện là số có tổng các ước số của nó (không kể nó) thì bằng chính nó.
# Vd: 6 có các ước số là 1,2,3 và 6=1+2+3 ➔6 là số hoàn thiện)
# b) Kiểm tra số nguyên dương n có phải là số thịnh vượng (Abundant number)hay
# không? (Số thịnh vượng là số có tổng các ước số của nó (không kể nó) thì lớn hơn
# nó. Vd:12 có các ước số là 1,2,3,4,6 và 12<1+2+3+4+6 ➔12 là số thịnh vượng)

def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def is_perfect_number(n):
    if n <= 0:
        return False
    return sum_of_divisors(n) == n

def is_abundant_number(n):
    if n <= 0:
        return False
    return sum_of_divisors(n) > n
num = int(input("Nhap so nguyen duong n: "))
if is_perfect_number(num):
    print(f"{num} la so hoan thien")
if is_abundant_number(num):
    print(f"{num} la so thinh vuong")
else:
    print(f"{num} khong phai la so thinh vuong") 