

# (1) 给你一个list[int],判断这个数组是否是一个山峰(int值先变大，然后再变小)
    例如： [1,3,9,2,1]   ->yes
          [1,2,3,4,5]   ->no
          [1,2,1,2,1,2] ->no

    def solve(arr:list[int])->bool:
        cnt1,cnt2 = 0,0
        for i in range(2,len(arr)):
            if arr[i-2] < arr[i-1] > arr[i]:
                cnt1 += 1
            if arr[i-2] > arr[i-1] < arr[i]:
                cnt2 += 1
        return cnt1 == 1 and cnt2 == 0
    
    # 测试
    A = [1,3,9,2,1]
    B = [1,2,3,4,5]
    C = [1,2,1,2,1,2]
    print(solve(A)) # true
    print(solve(B)) # false
    print(solve(C)) # false

# (2) 给你两个长度一样的字符串s，t，将里面的字符进行交替，形成一个新的字符串，然后再返回
    例如：s: abc t:def  ->  adbecf

# (3) 给你两个长度一样且是偶数长度的字符串s，t，将里面的每2个字符进行交替，形成一个新的字符串，然后再返回
    例如：s: abcd t:xyzu  ->  abxycdzu

# (4) 给你两个有序(从小到大)数组，将这两个数组合并成一个有序数组,然后返回
    例如：arr1 = [1,2,3] arr2 = [2,4,9,11] ->合并后[1,2,2,3,4,9,11]

# (5) 给你3个int类型的变量a,b,c，问是否可以由这三个变量作为边长形成一个等腰三角形

# (6) 给你一个由多个单词组成的字符串，单词之间用单个空格组成，请把其中的单词进行翻转，然后以一个字符串形式返回
    例如："hello world code" -> "olleh dlrow edoc"
# (7) 给你一个由多个单词组成的字符串，单词之间用多个空格组成,前后也会有空格，请把其中的单词进行翻转，然后以一个字符串形式返回
    例如："hello   world code  " -> "olleh   dlrow edoc  "
    def solve(s:str)->str:
        ans = ""
        cur = ""
        for c in s:
            if c.isalpha():
                cur += c
            else:
                if len(cur) > 0:
                    ans += cur[::-1]
                    cur = ""
                ans += c
        if len(cur) > 0:
            ans += cur[::-1]
        return ans
    
    s = "hello   world code" # output: olleh   dlrow edoc
    print(solve(s))
# (8) 给你一个list[str],里面的str全部是数字字符串，请按照字符串的实际int进行从大到小排序，然后返回
    例如: ["123","25","777"] -> ["25","123","777"]
    
# (9) 给你两个哈希表，把这两个哈希表进行合并，然后再返回