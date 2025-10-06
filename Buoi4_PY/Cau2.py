from random import randrange
while True:
    somay=randrange(1,101)
    solandoan=0
    win=False
    while solandoan<7:
        solandoan+=1
        songuoi=int(intput("Máy đoán [1..101], mời bạn đoán:"))
        print("Bạn đoán lần thứ ", solandoan)
        if somay=songuoi:
            print("Chúc mừng bạn đoán đúng, số máy là: ", somay)
            win=True
            break
        if somay>songuoi