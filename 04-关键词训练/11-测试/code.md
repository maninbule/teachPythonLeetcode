

# (1) 给你一个字符串，输出一共有多少个小写字母没有出现过
    s = "abc134"
    st = set()
    for c in s:
        if c.islower():
            st.add(c)
    print(26 - len(st))

    s = "ab134c"
    st = set(s)
    not_existed = 0
    for ascii in range(ord('a'),ord('z') + 1):
        c = chr(ascii)
        if c not in st:
            not_existed += 1
    print(not_existed)

# (2) 给你一个int类型变量x，输出x的个位数字。 比如123的个位数字为3
    print(abs(x)%10)
# (3) 给你一个list[list[int]] ,其中list[int]包含3个元素，请按照下标为1的元素进行从大到小排序
    例如：[[1,2,3],[4,5,6],[2,3,1]]->[[4,5,6],[2,3,1],[1,2,3]]
    arr = [[1,2,3],[4,5,6],[2,3,1]]
    arr.sort(key=lambda x:-x[1])
    print(arr)
# (4) 给你一个大于等于0的y，问至少2的多少次方，可以大于等于y，也就是2^x >= y，求最小的x
    
# (5) 给你一个n，初始化一个大小为nxn的矩阵arr，其两条对角线的元素都为1，其他都是0，请打印出这个矩阵
    n = 4
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        # 对角线1
        arr[i][i] = 1
        # 对角线1
        arr[i][n-i-1] = 1
    for line in arr:
        print(line)

# (6) 给你一个数x，判断x是否是质数，质数是除1以外的正整数，且只能被1和自身整除
    def is_prime(x:int)->bool:
        if x == 1:
            return False
        for y in range(2,x):
            if x % y == 0:
                return False
        return True
    
    print(is_prime(17)) # 16 = 8 * 2
# (7) 把1到100中的所有质数，从小到大保存到一个list[int]中，并输出
    def is_prime(x:int)->bool:
        if x == 1:
            return False
        for y in range(2,x):
            if x % y == 0:
                return False
        return True
    ans = 0
    for i in range(1,101):
        if is_prime(i):
            ans += 1
    print(ans)
# (8) 给你一个字符串s，判断一共有多少对相邻的4元素，4个字符完全不同
    
# (9) 给你一个字符串s，问是否可以切分成3段，每一段都相同
    例如:abcabcabc ->yes
    
    s = "abcabcabc"
    
    def judge(s:str)->bool:
        n = len(s)
        if n % 3 != 0:
            return False
        k = n//3
        return s[:k] == s[k:2*k] == s[2*k:]
    
    # [0,k-1] [k,2*k-1] [2k,n-1]
    
    # k = 3
    # [0,2] [3,5] [6,8]
    
    print(judge(s))
# (10) 给你一个只包含小写字母的字符串s，输出一个字符串，输出的字符串是字符串s的排序版本，也就是字母从小到大排序好了
    例如:输入: acbd 输出: abcd
    s = "abcabcabc"
    s = list(s)
    s.sort()
    print("".join(s))