


# (1) 判断一个字符串s是否是回文字符串,回文字符串就是正着读和反着读是一样的
    return s == s[::-1]
# (2) 给你一个int类型的数组，输出任意一个出现次数最多的那个数
    arr = [1,2,2,3,3,3]
    from collections import defaultdict
    cnt = defaultdict(int)
    ans = arr[0]
    max_cnt = 1
    for x in arr:
        cnt[x] += 1
        if cnt[x] > max_cnt:
            max_cnt = cnt[x]
            ans = x
    print(ans)
# (3) 给你两个int类型的set A, B, 请将A和B合并成set C，并输出C中的元素
    A = {1,2,3}
    B = {2,3,4,5}
    C = set()
    for x in A:
        C.add(x)
    for x in B:
        C.add(x)
    print(C)
# (4) 给你两个int类型的defaultdict A, B, 请将A和B合并成faultdict C，并输出C中的元素，相同的key，则value相加
    from collections import defaultdict
    A = defaultdict(int)
    B = defaultdict(int)
    A[1] = 2
    A[2] = 3
    
    B[2] = 4
    B[3] = 5
    
    C = defaultdict(int)
    for key,value in A.items():
        C[key] += value
    for key,value in B.items():
        C[key] += value
    
    print(C)

# (5) 创建一个二维数组，大小为nxm,并且从上往下，从左往右，依次递增，起点为1,每次增加1
    例子： n = 3,m = 4
    输出: [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    
# (6) 给你两个长度一样的字符串，判断对应位置，有多少个不同的字符
    例如："abc" "acc" 则输出1
    
# (7) 给你一个字符串s，输出任意一个出现次数第2多的字符
    例如："abbccc" 输出b
    s = "abbccc"
    from collections import defaultdict
    cnt = defaultdict(int)
    for c in s:
        cnt[c] += 1
    arr = []
    for c,times in cnt.items():
        arr.append([c,times])
    arr.sort(key=lambda x:-x[1])
    print(arr[1][0])
# (8) 给你一个字符串s，里面只有小写字母，输出里面出现的(1-26)序号最大的字母
    例如： "agdwf" 输出w
    s = "agdwf"
    ans = None
    for ascii in range(ord('z'),ord('a')-1,-1):
        c = chr(ascii)
        if c in s:
            ans = c
            break
    print(ans)
    第二方法：
    s = "agdwf"
    s_list = list(s)
    s2_list = sorted(s_list)
    print(s2_list[-1])
# (9) 给你list[list[int]]的数组，请按其中元素的第0位元素进行从大到小排序
    例如：[[1,2],[3,2],[2,1]] -> 排序后[[3,2],[2,1],[1,2]]
    arr = [[1,2],[3,2],[2,1]]
    arr.sort(key=lambda x:-x[0])
    print(arr) 

# (10) 给你一个int类型的数x，判断这个数是否是质数，(质数就是只能被1和自身整除的数，除了1)
    x = 17
    isPrime = True
    for y in range(2,x):
        if x % y == 0:
            isPrime = False
            break
    if isPrime:
        print("yes")
    else:
        print("no")
