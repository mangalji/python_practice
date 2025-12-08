# def fibo(n):
# 	if n == 0 or n == 1:
# 		return n
# 	elif n < 0:
# 		return "wrong input!!"
# 	else:
# 		return fibo(n-1) + fibo(n-2)

# num = int(input("enter the number input"))
# print(fibo(num))

# class Solution:
def fib(n: int) -> int:
    if n==0 or n==1:
        return n
    a=0
    b=1
    for i in range(2, n+1):
        a,b = b,a+b    
    return b
n = 7
print(fib(n))