

# (1) 给你一个二维数组list[list[str]],其中的str只有一个字母，请把里面每一个3x3大小的区域
    的字符从上到下，从左到右拼在一起成一个9个字母的字符串，保存到list[str]中，进行返回
    输入：
    arr  = [
        ['a','b','c','d'],
        ['a','b','c','d'],
        ['a','b','c','d'],
        ['a','b','c','d'],
    ]
    输出：
        ['abcabcabc','bcdbcdbcd','abcabcabc','bcdbcdbcd']

# (2) 现在需要你安排一些人进行排队，一共有这些操作：
    [1,name] 表示从队伍左边进一个名字叫a的人
    [2,name] 表示从队伍右边进一个名字叫a的人
    [3,None] 表示从队伍左边出去一个人
    [4,None] 表示从队伍右边出去一个人
    给你一个list[[操作，名字|None]]这样的数组，将这些操作全部执行，最后返回这个队伍
    输入:
    [[1,'a'],[1,'b'],[2,'c'],[2,'d'],[3,None],[4,None],[1,'e']]
    输出:
    ['e',a','c']
    from collections import deque
    
    def solve(arr:list[list])->list[str]:
        q = deque()
        for op in arr:
            if op[0] == 1:
                q.appendleft(op[1])
            elif op[0] == 2:
                q.append(op[1])
            elif op[0] == 3:
                q.popleft()
            else:
                q.pop()
        ans = []
        while len(q) > 0:
            ans.append(q.popleft())
        return ans
    input = [[1,'a'],[1,'b'],[2,'c'],[2,'d'],[3,None],[4,None],[1,'e']]
    print(solve(input))
# (3) 给你一个list[int]表示这些数字是以这样的顺序出栈，他们入栈的时候是按从小到大顺序入栈的
    问这样的出栈次序是否合法
    输入：[1,3,2,4]
    输出：true   解释：1 入栈 1 出栈 2 入栈 3入栈 3出栈 2出栈 4入栈 4出栈
# (4) 现在给你一些学生成绩(语文，数学，英文)这样的三元组，以list[list[int]]形式给你，
    请写一个优先队列，来实现成绩的排序，优先按照总分进行排序，其次按照单科成绩最高分排序
    解释：也就是定义好优先队列的节点node，让这些成绩变成node，先全部入优先队列，然后全部出来就排序了
    def solve(arr:list[list[int]])->list[list[int]]:
        from queue import PriorityQueue
        class node:
            def __init__(self,s:list[int]):
                self.s = s
            def __lt__(self, other):
                if sum(self.s) != sum(other.s):
                    return sum(self.s) > sum(other.s)
                else:
                    return max(self.s) > max(other.s)
        q = PriorityQueue()
        for s in arr:
            q.put(node(s))
        ans = []
        while q.qsize() > 0:
            cur_node = q.get()
            ans.append(cur_node.s)
        return ans
    
    input = [[89,90,50],[100,100,100],[87,92,50]]
    print(solve(input))
# (5) 请你写一个class，实现一个简化版的图书管理系统，里面有以下功能：
    1. 添加一本书
    2. 借出一本书
    3. 用list[str]返回现在还没有被借出去的书
    4. 用list[str]返回现在被借出去的书
    5. 返回被借阅次数最多的3本书的名字

    另外：图书只用记录名字，每本图书的名字都不一样
    from collections import defaultdict
    class BookManageMent:
        def __init__(self):
            self.havebook = dict()
            self.check_out_times = defaultdict(int)
        def addbook(self,title:str):
            self.havebook[title] = True
        def check_out_book(self,title:str):
            self.havebook[title] = False
            self.check_out_times[title] += 1
        def list_have_book(self)->list[str]:
            have = []
            for title,value in self.havebook.items():
                if value == True:
                    have.append(title)
            return have
        def list_check_out_book(self)->list[str]:
            have = []
            for title,value in self.havebook.items():
                if value == False:
                    have.append(title)
            return have
        def list_top3_book(self):
            check_out_book = []
            for key in self.check_out_times.keys():
                check_out_book.append(key)
            check_out_book.sort(key=lambda title:-self.check_out_times[title])
            return check_out_book[:min(3,len(check_out_book))]
    
    bm = BookManageMent()
    bm.addbook("bookA")
    bm.addbook("bookB")
    bm.addbook("bookC")
    bm.addbook("bookD")
    bm.addbook("bookE")
    print(bm.list_have_book())
    bm.check_out_book("bookB")
    print(bm.list_have_book())
    print(bm.list_check_out_book())
    bm.addbook("bookB")
    bm.check_out_book("bookB")
    bm.check_out_book("bookA")
    bm.addbook("bookA")
    bm.check_out_book("bookE")
    bm.check_out_book("bookD")
    print(bm.list_top3_book())












    