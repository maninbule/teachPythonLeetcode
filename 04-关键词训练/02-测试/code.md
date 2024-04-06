

# (1) 判断一个字符x是否是字母，是的话，输出yes，不是的话，输出no

# (2) 从字符串s中取出一个子串，子串的下标区间为[left,right]

# (3) 输出一个字符串s中有多少个不同的字符

# (4) 输出int类型列表arr的中间的那个元素

# (5) 使用循环，从-1循环到-10，并打印

# (6) 创建一个长度为n的int类型数组，让数组的元素全部都是1

# (7) 判断a的三次方 + b的平方是否等于c的4次方，是的话，输出yes，否则no

# (8) 将一个数组arr，按照从大到小进行排序
    arr = [1,32,1,23,5]
    arr.sort(reverse=True)
    print(arr)
# (9) 判断字符变量a,b,c,d,e是否全都不同，全部不同输出yes，否则no
    a,b,c,d,e = 'a','b','c','t','e'
    st = {a,b,c,d,e}
    if len(st) == 5:
        print('yes')
    else:
        print("no")
# (10) 统计一个字符串s中字母a到z各出现了多少次
    from collections import defaultdict
    s = "=hello world+"
    cnt = defaultdict(int)
    for c in s:
        cnt[c] += 1
    for ascii in range(ord('a'),ord('z') + 1):
        c = chr(ascii)
        print(c,cnt[c])

