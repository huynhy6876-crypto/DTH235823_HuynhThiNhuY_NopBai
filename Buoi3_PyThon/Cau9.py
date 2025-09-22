month = int(input("Nhập vào số tháng (1-12): "))

if 1 <= month <= 3:
    print(f"Tháng {month} thuộc quý 1.")
elif 4 <= month <= 6:
    print(f"Tháng {month} thuộc quý 2.")
elif 7 <= month <= 9:
    print(f"Tháng {month} thuộc quý 3.")
elif 10 <= month <= 12:
    print(f"Tháng {month} thuộc quý 4.")
else:
    print("Tháng không hợp lệ. Vui lòng nhập số từ 1 đến 12.")