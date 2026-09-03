import time

# 순환적 구조

def fib(n): 
    if n == 0 or n==1:
        return n
    else:
        return fib(n-2) + fib(n-1)

#반복적 구조

def fib_iter(n):
    if n == 0 or n==1:
        return n
    else: return n
    a,b = 0,1
    i = 1
    while i < n:
        a,b=b ,a+b
        i+= 1
        return b

print(f'피보나치 반복({5}) = {fib_iter(5)}')
print(f'피보나치 순환({5}) = {fib(5)}')

for i in range(1,40):
        start = time.time()
        fib(i)
        time_rec = time.time() - start

        start_iter = time.time()
        fib_iter(i)
        time_iter = time.time() - start_iter

        print(f"n= {i}   반복: {time_iter:.2f} 순환: {time_rec:.2f}")
