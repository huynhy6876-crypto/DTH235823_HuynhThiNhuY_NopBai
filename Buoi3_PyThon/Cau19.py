import math

def tinh_tong_S(x, n):
    """
    Tính tổng S(x, n) = x^3/3! + x^5/5! + ... + x^(2n+1)/(2n+1)!
    
    Args:
        x (float): Giá trị x
        n (int): Số hạng cuối cùng
    
    Returns:
        float: Giá trị của tổng S(x, n)
    """
    tong = 0.0
    for k in range(1, n + 1):
        # Tính mũ: 2k + 1
        mu = 2 * k + 1
        # Tính giai thừa của mu
        giai_thua = math.factorial(mu)
        # Tính hạng k: x^(2k+1) / (2k+1)!
        hang_k = (x ** mu) / giai_thua
        tong += hang_k
        print(f"Hạng {k}: x^{mu}/({mu}!) = {hang_k:.6f}")
    
    return tong

def main():
    print("=== CHƯƠNG TRÌNH TÍNH TỔNG S(x, n) ===")
    print("S(x, n) = x³/3! + x⁵/5! + ... + x^(2n+1)/(2n+1)!")
    
    try:
        # Nhập dữ liệu từ người dùng
        x = float(input("Nhập giá trị x: "))
        n = int(input("Nhập giá trị n: "))
        
        if n < 1:
            print("Lỗi: n phải >= 1")
            return
        
        print(f"\nTính S({x}, {n}):")
        print("-" * 40)
        
        # Tính tổng
        ket_qua = tinh_tong_S(x, n)
        
        print("-" * 40)
        print(f"Kết quả: S({x}, {n}) = {ket_qua:.8f}")
        
        # Hiển thị thêm thông tin
        print(f"\nThông tin:")
        print(f"- x = {x}")
        print(f"- n = {n}")
        print(f"- Số hạng cuối: x^({2*n+1})/({2*n+1}!)")
        
    except ValueError:
        print("Lỗi: Vui lòng nhập số hợp lệ!")
    except Exception as e:
        print(f"Lỗi: {e}")

# Chạy chương trình
if __name__ == "__main__":
    main()