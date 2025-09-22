def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def next_day(day, month, year):
    # Số ngày trong từng tháng
    days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    day += 1
    if day > days_in_month[month - 1]:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return day, month, year

# Nhập ngày, tháng, năm
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

# Tìm ngày kế tiếp
next_d, next_m, next_y = next_day(day, month, year)
print(f"Ngày kế tiếp là: {next_d}/{next_m}/{next_y}")