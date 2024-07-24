
def getAvg(matrix,x1,y1,x2,y2):
    total = 0
    cnt = 0
    for i in range(x1,x2 + 1):
        for j in range(y1,y2 + 1):
            if matrix[i][j] >= 0:
                cnt += 1
                total += matrix[i][j]
    if cnt == 0:
        return -1
    return total//cnt
def solution(matrix:list[list[int]])->list[int]:
    dif = int(1e18)
    res = [0,0]
    n,m = len(matrix),len(matrix[0])
    for i in range(n-1):
        for j in range(m-1):
            sumarr = [0] * 4
            sumarr[0] = getAvg(matrix,0,0,i,j)
            sumarr[1] = getAvg(matrix,0,j + 1,i,m-1)
            sumarr[2] = getAvg(matrix,i + 1,0,n-1,j)
            sumarr[3] = getAvg(matrix,i + 1,j + 1,n-1,m-1)
            sumarr.sort()
            cur = sumarr[-1] - sumarr[0]
            if cur < dif and sumarr[0] != -1:
                dif = cur
                res = [i,j]
    return res

m = [
    [8,9,-1,-1],
    [3,8,-1,-1],
    [5,5,7,-1],
]
m = [
    [-1,-1,-1,-1],
    [0,-1,0,-1],
    [-1,0,0,0],
    [0,-1,-1,-1],
    [0,0,0,-1],
    [0,0,-1,0],
    [0,-1,-1,-1],
    [0,0,-1,-1],
    [-1,0,-1,-1],
]
print(solution(m))