
def solution(visits,target):
    total = 0
    for i in range(len(visits)):
        total += visits[i]
        if total >= target:
            return i
    return -1

print(solution([300,200,100,200,500],700))
print(solution([700,800,500],2001))