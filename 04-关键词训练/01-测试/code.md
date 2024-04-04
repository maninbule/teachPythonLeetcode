

# (1) 创建一个长度为n的int类型数组,数组名为arr
        n = 6
        arr = [0] * n
# (2) 使用for循环遍历[1,n]之间的所有奇数，循环变量为x
        for x in range(1,n+1):
            print(x)
# (3) 对一个字符串按照空格进行拆分，字符串为s，拆分之后保存的名字叫arr
            s= 'i am Guanyu'
            arr = s.split()
# (4) 将一个字符串列表arr使用字符+号进行拼接
            ans = '+'.join(arr)
# (5) 对一个int类型的列表进行求和，把求和的内容保存在sum变量中
            arr = [1,2,3,4,5]
            sum = 0
            for x in arr:
                sum += 1
# (6) 写一个循环，从字母a遍历到字母z，并打印出来
            for i in range(ord('a'),ord('z'))
                print(i)
# (7) 将一个字符串s，转换成int类型
                s = "123"
                ans = int(s)
# (8) 判断x是否是y的倍数，是的话，输出yes，如果不是输出no
        x= 15
        y =5
        if x % y == 0:
            return 'yes'
        else:
            return 'no'
# (9) 输出数组arr的最后一个元素的值
        return arr[:: -1]
# (10) 将一个数组arr进行翻转
    L,R= 0,len(arr)-1
    while L<R:
        arr[L],arr[R] = arr[R],arr[L]
        L+=1
        R-=1
    return arr