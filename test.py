
my_set = eval(input())
res = 0
for v in my_set:
    if abs(v) < 10:
        res += v
print(res)