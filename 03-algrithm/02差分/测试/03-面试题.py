'''
给你每一辆车的在时刻上出现的时间区间，问每一时刻存在多少俩车？

intput = [[1,3],[2,5],[3,4]]
output = [1,2,3,2,1]
'''

# prefixsum and difference array

def countcars(arr:list[list[int]])->list[int]:
    mxtime = 0
    for interval in arr:
        mxtime = max(mxtime,interval[1])
    diff = [0] * (mxtime + 10)
    for interval in arr:
        diff[interval[0]] += 1
        diff[interval[1] + 1] -= 1
    prefixsum = [0] * (mxtime + 1)
    for i in range(1,mxtime + 1):
        prefixsum[i] = prefixsum[i-1] + diff[i]
    return prefixsum[1:]

print(countcars([[1,3],[2,5],[3,4]]))

