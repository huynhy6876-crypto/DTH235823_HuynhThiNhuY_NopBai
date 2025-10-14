def fibonacii(n):
    if n<=2:
        return 1
    return fibonacii(n-1)+fibonacii(n-2)
def listfibo(n):
    for i in range(1,n+1):
        print(fibonacii(i),end='\t' )
print(fibonacii(9))
listfibo(9)        