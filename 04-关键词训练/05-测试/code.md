

# (1) 给你一个int，输出这个int有几位数

# (2) 给你一个字符串s，去除字符串中的所有数字，然后输出剩余的字符串

# (3) 给你一个int类型的set，将set里面的int装到一个list里面去

# (4) 给你一个int类型的list，将list第一个和最后一个去掉，保留中间的,并返回
    return arr[1:len(arr)-1]

# (5) 给你一个字符串s，判断字符串中是否有3个相同的字符,如果有输出yes，否则no
    from collections import defaultdict
    cnt = defaultdict(int)
    for c in s:
        cnt[c] += 1
        if cnt[c] >= 3:
            return 'yes'
    return 'no'
    
# (6) 给你一个int类型的数组arr，判断所有奇数下标的元素求和是否等于所有偶数下标元素求和

# (7) 给你一个数组arr，判断是否这个数组中的元素各不相同

# (8) 给你一个数组arr，和一个int类型的x，判断arr中是否存在x
    for a in arr: # 数组 O(n*k)
        if a == x:
            return True
    return False
    
    # 优化：可以用set优化
    st = set(arr) # O(n)
    if x in st: # O(k)
        return True
    return False
    O(n + k)
# (9) 给你两个字符串s，t，将s和t拼接成一个新的字符串k，并把k输出
    
# (10) 给你三个int类型的变量a,b,c, 判断是否可以由a，b，c作为边长组成一个三角形

