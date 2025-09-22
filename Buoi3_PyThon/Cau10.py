import math

def tinh_tong_chuoi(x, n):
    """
    Tính tổng S(x,n) = x + x²/2! + x³/3! + ... + xⁿ/n!
    
    Args:
        x (float): Giá trị x
        n (int): Số hạng cuối cùng
    
    Returns:
        float: Tổng của chuỗi
    """
    tong = 0.0
    print(f"Tính S({x}, {n}) = x + x²/2! + x³/3! + ... + xⁿ/n!")
    print("-" * 50)
    
    # Tính từng hạng tử và cộng dồn
    for i in range(1, n + 1):
        # Hạng tử thứ i: x^i / i!
        hang_tu = (x ** i) / math.factorial(i)
        tong += hang_tu
        
        # In từng hạng tử
        print(f"Hạng thứ {i}: x^{i}/{i}! = {x}^{i}/{i}! = {hang_tu:.6f}")
    
    print(f"Tổng S({x}, {n}) = {tong:.6f}")
    print("-" * 50)
    return tong

# Chương trình chính
def main():
    print("=== CHƯƠNG TRÌNH TÍNH TỔNG CHUỖI SỐ ===")
    print("Công thức: S(x,n) = x + x²/2! + x³/3! + ... + xⁿ/n!")
    
    # Nhập dữ liệu từ người dùng
    try:
        x = float(input("\nNhập giá trị x: "))
        n = int(input("Nhập số hạng n: "))
        
        if n < 1:
            print("Số hạng n phải >= 1!")
            return
        
        # Tính và hiển thị kết quả
        ket_qua = tinh_tong_chuoi(x, n)
        
        print(f"\nKẾT QUẢ CUỐI CÙNG:")
        print(f"S({x}, {n}) = {ket_qua:.6f}")
        
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")

# Test với một số trường hợp mẫu
def test_truong_hop():
    print("=== TEST CÁC TRƯỜNG HỢP MẪU ===")
    
    test_cases = [
        (2, 3),   # S(2,3)
        (3, 4),   # S(3,4)
        (1, 5),   # S(1,5)
        (0, 3),   # S(0,3)
        (-2, 3),  # S(-2,3)
    ]
    
    for x, n in test_cases:
        print(f"\nTrường hợp: x = {x}, n = {n}")
        tinh_tong_chuoi(x, n)

# Chạy chương trình
if __name__ == "__main__":
    # Chạy test trước
    test_truong_hop()
    
    # Sau đó chạy chương trình tương tác
    print("\n" + "="*60)
    main()