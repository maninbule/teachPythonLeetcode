# factorial of given number

'''
计算n的阶乘
n! = n x (n-1) x (n-2) .... 1
'''
def factorial(n:int)->int:
    ans = 1
    for i in range(n,0,-1):
        ans *= i
    return ans

print(factorial(5))