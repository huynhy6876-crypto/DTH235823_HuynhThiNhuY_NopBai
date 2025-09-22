# Chương trình tìm giá trị nhỏ nhất trong 3 biến i, j, k
def tim_gia_tri_nho_nhat(i, j, k):
    """
    Tìm giá trị nhỏ nhất trong 3 biến i, j, k
    và in ra kết quả
    """
    
    # Bước 1: So sánh i và j
    if i < j:
        # Nếu i nhỏ hơn j thì so sánh i với k
        if i < k:
            gia_tri_nho_nhat = i
        else:
            gia_tri_nho_nhat = k
    else:
        # Nếu j nhỏ hơn hoặc bằng i thì so sánh j với k
        if j < k:
            gia_tri_nho_nhat = j
        else:
            gia_tri_nho_nhat = k
    
    # In kết quả
    print(f"i = {i}, j = {j}, k = {k}")
    print(f"Giá trị nhỏ nhất là: {gia_tri_nho_nhat}")
    print("-" * 30)

# Test các trường hợp
print("KẾT QUẢ CHO CÁC TRƯỜNG HỢP:")

# Trường hợp (a): i=3, j=5, k=7
print("(a) i=3, j=5, k=7")
tim_gia_tri_nho_nhat(3, 5, 7)

# Trường hợp (b): i=3, j=7, k=5
print("(b) i=3, j=7, k=5")
tim_gia_tri_nho_nhat(3, 7, 5)

# Trường hợp (c): i=5, j=3, k=7
print("(c) i=5, j=3, k=7")
tim_gia_tri_nho_nhat(5, 3, 7)

# Trường hợp (d): i=5, j=7, k=3
print("(d) i=5, j=7, k=3")
tim_gia_tri_nho_nhat(5, 7, 3)

# Trường hợp (e): i=7, j=3, k=5
print("(e) i=7, j=3, k=5")
tim_gia_tri_nho_nhat(7, 3, 5)

# Trường hợp (f): i=7, j=5, k=3
print("(f) i=7, j=5, k=3")
tim_gia_tri_nho_nhat(7, 5, 3)