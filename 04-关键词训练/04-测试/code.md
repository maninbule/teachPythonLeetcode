
# (1) 给你一个n个元素int类型的数组arr，判断这个数组是不是从1到n依次严格递增
    # arr[i] ?= i + 1
    for i in range(len(arr[i])):
        if arr[i] != i + 1:
            return False
    return True
# (2) 给你一个字符串s，返回这个字符串有多少个不同的数字字符
    st = set()
    for c in s:
        if c.isdigit():
            st.add(c)
    return len(st)
# (3) 给你一个字符串，将这个字符串里面的数字全部替换成空格，然后输出
    
# (4) 给你一个int类型的数组，判断这个数组里面是否存在2个相同的元素，如果存在输出yes,否则no
    for i in range(len(arr)):
        for j in range(i + 1,len(arr)):
            if arr[i] == arr[j]:
                return 'yes'
    return 'no'
# (5) 给你一个int类型的数组，将这个数组进行从大到小排序，然后输出
    arr = [1,3,2]
    arr.sort(key = lambda x:-x)
# (6) 给你一个int类型的数组，下标从0开始，按下标递增的顺序，输出下标为偶数的元素
    
# (7) 给你一个int类型数组，判断是否存在三个元素a，b，c，满足a + b = c,如果存在输出Yes，否则no
    
# (8) 给你两个int类型数组，将这两个数组合并到一起，然后输出
    
# (9) 输出一个存储的字母的c变量的ascii编码

# (10) 给你一个ascii编码，输出他对应的字符