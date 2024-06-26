'''
给你一些数字，请输出其中出现次数超过一半的那个数字
如果不存在，则返回空

输入：
1 3 2 3 6 3 3
输出：
3
输入：
1 2 3 4 5
输出：
None
'''

def solve(nums:list[int]):
    win = None
    cnt = 0
    for x in nums:
        if x != win:
            cnt -= 1
            if cnt <= 0:
                win = x
                cnt = 1
        else:
            cnt += 1
    cnt = 0
    for x in nums:
        if x == win:
            cnt += 1
    if cnt * 2 > len(nums):
        return win
    return None

input = [1, 3, 2, 3, 6, 3 ,3]
print(solve(input))

input = [1,2,3,4,5]
print(solve(input))

input = []
print(solve(input))

input = [1]
print(solve(input))

input = [2,2,3,3]
print(solve(input))