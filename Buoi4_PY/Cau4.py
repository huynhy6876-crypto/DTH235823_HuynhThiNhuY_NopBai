def ROI(dt,cp):
    return (dt-cp)/cp
def GoiYDauTu(roi):
    if roi>=0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"
print("Chương trình tính ROI")
dt=int(input("Nhập doanh thu: "))
cp=int(input("Nhập chi phí: "))
roi=ROI(dt,cp)
print("Tỉ suất lợi nhuận ROI là: ",roi)
print("==>",GoiYDauTu(roi))    
    