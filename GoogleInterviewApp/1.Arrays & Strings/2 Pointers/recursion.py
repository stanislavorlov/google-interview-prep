def printLoop(num):
    if num == 0:
        return
    printLoop(num-1)
    print(num)
    
printLoop(10)
print("fibonaci")

def fibonaci(n):
    return 0 if n == 0 else 1 if n == 1 else fibonaci(n-1) + fibonaci(n-2)

print(fibonaci(0))
print(fibonaci(1))
print(fibonaci(2))
print(fibonaci(3))
print(fibonaci(4))
print(fibonaci(5))