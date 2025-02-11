from time import time


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
print(factorial(15))

def bad_fibonaci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonaci(n-2) + bad_fibonaci(n-1)

start_time = time()
print(bad_fibonaci(50))
print(bad_fibonaci(150))
stop_time = time()
elapsed = stop_time - start_time

print("bad fibonaci: " + str(elapsed))

def good_fibonaci(n):
    if n <= 1:
        return (n, 0)
    else:
        (a,b) = good_fibonaci(n-1)
        return (a+b,a)
    
start_time = time()
print(good_fibonaci(50))
print(good_fibonaci(150))
stop_time = time()
elapsed = stop_time - start_time

print("good fibonaci: " + str(elapsed))