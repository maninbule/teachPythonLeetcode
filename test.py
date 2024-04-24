from functools import cache
import sys
sys.setrecursionlimit(10000)  # 设置最大递归次数为10000
@cache
def fib(n:int )->int:
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2) # fib(n) -> res

print(fib(1000))