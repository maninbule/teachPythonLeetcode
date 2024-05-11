'''
给你一个int类型的数x，你最多可以修改k次某一个数位，问能通过修改之后能变成的最大数字是多少

input: x = 134 k = 1
output: 934

input: x = 992956 k = 2
output: 999996

input: x = -104 k = 2

input: x = 0 k = 10
output: 9
'''

def solve(x:int,k:int)->int:
    if k == 0:
        return x
    if x >=0:
        arr = list(str(x))
        for i in range(len(arr)):
            if arr[i] != '9':
                arr[i] = '9'
                k -= 1
                if k == 0:
                    break
        return int("".join(arr))
    else:
        arr = list(str(x))
        if len(arr) == 2:
            return 0
        if arr[1] != '1':
            arr[1] = '1'
            k -= 1
        for i in range(2,len(arr)):
            if arr[i] != '0' and k > 0:
                arr[i] = '0'
                k -= 1
        return int("".join(arr))

x = 134
k = 1
print(solve(x,k)) # output: 934

x = 992956
k = 2
print(solve(x,k)) # output:999996

x = -7
k = 2
print(solve(x,k)) # output:0

x = -227
k = 2
print(solve(x,k)) # output:-107

x = -100
k = 2
print(solve(x,k)) # output:-100

x = -110
k = 99999
print(solve(x,k)) # output:-100

x = 0
k = 99999
print(solve(x,k)) # output:9

x = 0
k = 0
print(solve(x,k)) # output:0