"""Tính điểm trung bình-Viết chương trình nhập vào điểm ba môn Toán, Lý, Hóa của một học sinh. In ra
điểm trung bình của học sinh đó với hai số lẻ thập phân."""
toan=float(input("Nhập điểm Toán:"))
ly=float(input("Nhập điểm lý:"))
hoa=float(input("Nhập điểm hóa:"))
dtb=(toan+ly+hoa)/3
print("Điểm trung bình=",dtb)
print("Điểm trung bình=",round(dtb,2))