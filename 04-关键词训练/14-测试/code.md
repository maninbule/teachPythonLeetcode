
所有题目需要用函数来实现，然后调用函数来进行测试

# (1) 给你一个区间[L,R],问这个区间中有多少个奇数

# (2) 给你一个字符串s，去掉字符串中的所有空格，然后再返回

# (3) 给你两个区间[L1,R1],[L2,R2],问这两个区间是否出现了交叉

# (4) 给你两个区间[L1,R1],[L2,R2]，将交叉的那部分进行输出成一个新的区间

# (5) 给你两个区间[L1,R1],[L2,R2]，将两个区间进行合并，输出合并后的新区间

# (6) 给你一个list[int]，从左往右，将相邻2个元素进行相加，变成一个新的list[int]，返回这个list[int]
    保证输入的list[int]是偶数长度
    例如：输入: [1,2,3,4] 输出[3,7]

# (7) 给你一个List[str]，将里面的所有字符串的首尾字符去掉，保留中间的，再返回处理之后的list[str]
    保证输入的list[str]中的str长度大于等于2
    例如：输入: ["123","ab","afsggg","2224"] 输出["2","","fsgg","22"]

# (8) 给你一个字符串s，输出里面哪个字符出现的次数最多
    def solve(s:str)->str:
        from collections import defaultdict
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
        ans_char = s[0]
        for char,times in cnt.items():
            if times > cnt[ans_char]:
                ans_char = char
        return ans_char
    
    # 测试
    s = "abbbcccc" # out = c
    print(solve(s))
    s = "abbbccc" # out = b or c
    print(solve(s))
# (9) 给你一个list[list[int]],输出里面最大的list[int]的最大值
    # 输入[[1,2,3],[2,5,6],[1,4,2]] ->输出[3,6,4]

# (10) 给你一个list[list[int]],保证一定是个方阵，请你将所有对角线元素相加求和并输出

