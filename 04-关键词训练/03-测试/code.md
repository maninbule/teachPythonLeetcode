

# (1)给你一个int类型数组arr，将这个数组进行翻转
    arr = [1,2,3]
    arr = arr[::-1]
    方法2：
    left,right = 0,len(arr)
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    
# (2)给你一个字符串s，将字符串中的非数字字符用空格替换，然后打印出来
    ans = ""
    for c in s:
        if not c.isdigit():
            ans += ' '
        else:
            ans += c
# (3)给你一个字符串s，输出任意一个出现次数最多的那个字符
    from collections import defaultdict
    cnt = defaultdict(int)
    times,ans = 0,None
    for c in s:
        cnt[c] += 1
        if cnt[c] > times:
            times = cnt[c]
            ans = c
    print(ans)
# (4)给你一个int类型数组，如果这个数组是严格递增的，输出yes，否则no
    arr = [1,2,5,9]
    for i in range(len(arr)-1):
        if not arr[i] < arr[i+1]:
            return 'no'
    return 'yes'
        
# (5)给你一个int类型数组，如果这个数组全部元素都相等，输出yes，否则no
    st = set(arr)
    if len(st) == 1:
        return 'yes'
    else:
        return 'no'
# (6)给你一个int类型数组，输出这个数组中元素是3的倍数的个数
    ans = 0
    for x in arr:
        if x % 3 == 0:
            ans += 1
    return ans
# (7)创建一个长度为n的int类型数组，数组中的元素从1到n依次递增
    ans = [0] * n
    for i in range(0,len(ans)):
        ans[i] = i + 1
# (8)使用循环从10到2依次递减，输出其中的偶数
    for x in range(10,1,-1):
        print(x)
# (9)将一个int类型数组arr转换成一个集合set
    arr = [1,5,2,3,3]
    st = set(arr) # len(st) == 4
# (10) 将一个字符串s，转换成一个set
    s = "abbcc"
    st = set(s) # "abc" len(st) == 3
