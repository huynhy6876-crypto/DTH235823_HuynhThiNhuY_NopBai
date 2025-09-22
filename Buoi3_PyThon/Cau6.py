def doc_so(n):
    hang_don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 0 or n > 99:
        return "Số không hợp lệ"

    if n < 10:
        return hang_don_vi[n]
    elif n < 20:
        if n == 10:
            return "mười"
        elif n == 15:
            return "mười lăm"
        else:
            return "mười " + hang_don_vi[n % 10]
    else:
        chuc = n // 10
        don_vi = n % 10
        if don_vi == 0:
            return hang_chuc[chuc]
        elif don_vi == 1:
            return hang_chuc[chuc] + " mốt"
        elif don_vi == 5:
            return hang_chuc[chuc] + " lăm"
        else:
            return hang_chuc[chuc] + " " + hang_don_vi[don_vi]

n = int(input("Nhập số n (tối đa 2 chữ số): "))
print(doc_so(n))