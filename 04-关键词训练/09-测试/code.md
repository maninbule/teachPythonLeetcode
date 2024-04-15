

# (1) 给你两个int类型数组，输出两个数组中同时存在的元素

# (2) 给你两个int类型数组，输出两个数组中同时存在，且都出现了2次的元素
    arr1 = [1,1,2,2,3,3,3,4]
    arr2 = [1,1,2,2,3,3,3,4,5,6,6]
    
    from collections import defaultdict
    mp1 = defaultdict(int)
    mp2 = defaultdict(int)
    for x in arr1:
        mp1[x] += 1
    for x in arr2:
        mp2[x] += 1
    #--------------
    st = set(arr1)
    #-----------
    ans = []
    for x in st:
        if mp1[x] == mp2[x] == 2:
            ans.append(x)
    print(ans)
# (3) 给你一个正整数n，计算1 + 2 + 3 + .... +n的结果

# (4) 给你一个正整数n，输出n的所有约数 (如果n可以被x整除，那么x就是n的一个约数)

# (5) 给你一个正整数n，n可以开平方，问n开方之后等于多少

# (6) 给你三个正整数，a，b，c，问以a，b，c为边长，是否可以组成一个三角形
    arr = [a,b,c]
    arr.sort()
    if arr[0] + arr[1] > arr[2]:
        print('yes')
# (7) 给你一个int数组，输出数组中出现次数最少的那个数，如果有多个，输出最小的那个
    arr = [1,1,1,2,2,3,3,3,4,4,5,5]
    from collections import defaultdict
    mp = defaultdict(int)
    for x in arr:
        mp[x] += 1
    min_cnt,ans = None,None
    for key,times in mp.items():
        if min_cnt == None:
            min_cnt = times
            ans = key
        else:
            if times < min_cnt:
                min_cnt = times
                ans = key
            if times == min_cnt:
                ans = min(ans,key)
    print(min_cnt,ans)
# (8) 给你一个int数组，去掉一个最大值，去掉一个最小值，并保持原来的顺序，返回剩余元素
    arr = [1,2,3,4,5]
    ans = []
    min_value = min(arr) # O(n)
    max_value = max(arr) # O(n)
    min_removed,max_removed = False,False
    for x in arr:
        if x == min_value and not min_removed:
            min_removed = True
            continue
        if x == max_value and not max_removed:
            max_removed = True
            continue
        ans.append(x)
    print(ans)
# (9) 给你一个int数组，问每一个数，有多少个倍数在这个数组中出现，输出ans[i] 表示第i个数有ans[i]个倍数在数组中, 排除自身
    arr = [1,2,3,4,5]
    ans = [0] * len(arr)
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i == j:continue
            if arr[j] % arr[i] == 0:
                ans[i] += 1
    print(ans)

# (10) 给你两个字符串s,t，问t是否可以作为子串出现在s中

