'''
现在要分析每种股票的利润指标PNL
一种股票的利润指标指的是，当前卖出的时候，用的是最开始购买的股票，差价是自己的利润

时间   股票类型       行为        当前价格       数量
1     A             buy          5           100
2     A             buy          6           50
3     A             sell         10          110
4     A             sell         4           30

A股票的利润：
时间1： 买入股票A(5,100)
时间2： 买入股票A(6,50)
时间3： 卖出股票A(10,110) 此时赚的钱 = 10 *110 - 5*100 - 6*10 = 540
时间3： 卖出股票A(4,30) 此时赚的钱 = 4*30 - 6 * 30 = -60
A股票的利润指标为: 540 - 60 = 480
'''

class Share:
    def __init__(self,time:int,typeA:str,op:str,price:int,amount:int):
        self.time = time
        self.type = typeA
        self.op = op
        self.price = price
        self.amount = amount

def solve(record:list[Share])->list[(str,int)]:
    from collections import defaultdict,deque
    q = defaultdict(deque)
    earn = defaultdict(int)
    record.sort(key = lambda x:x.time)
    for r in record:
        if r.op == 'buy':
            q[r.type].append(r)
        else: # sell
            while r.amount > 0:
                front = q[r.type].popleft()
                if front.amount >= r.amount:
                    front.amount -= r.amount
                    earn[r.type] += r.amount * (r.price - front.price)
                    r.amount = 0
                    if front.amount > 0:
                        q[r.type].appendleft(front)
                    break
                else:
                    r.amount -= front.amount
                    earn[r.type] += front.amount * (r.price - front.price)
                    front.amount = 0
    res = []
    for t,e in earn.items():
        res.append([t,e])
    return res

'''
时间   股票类型       行为        当前价格       数量
1     A             buy          5           100
2     A             buy          6           50
3     B             buy          5           130
3     A             sell         10          110
4     A             sell         4           30
5     B             sell         2           30
6     B             sell         1           30
'''

input = [
    Share(1,'A','buy',5,100),
    Share(2,'A','buy',6,50),
    Share(3,'B','buy',5,130),
    Share(3,'A','sell',10,110),
    Share(4,'A','sell',4,30),
    Share(5,'B','sell',2,30),
    Share(6,'B','sell',1,30),
]

print(solve(input))