from math import sqrt
print ("Chương trình tính diện tích tam giác")
a=float(input("Nhập độ dài cạnh a: "))
b=float(input("Nhập độ dài cạnh b: "))
c=float(input("Nhập độ dài cạnh c: "))
if(a<=0 or b<=0 or c<=0) or (a+b<=c) or (a+c<=b) or (b+c<=a):
    print("Độ dài cạnh không hợp lệ")
else:
    cv=(a+b+c)/2
    p=cv/2
    dt=sqrt(cv*(cv-a)*(cv-b)*(cv-c))  
    print("Diện tích tam giác là: ",dt)  