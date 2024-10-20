''''''

'''
根据不同用户的购买物品历史，实时统计一周内最畅销的k件物品
Amazon.com 有一个“畅销产品”页面，您可以在其中查看最受欢迎的商品列表。

编写一个类，用于生成这些畅销商品的列表。您可以假设一个 Amazon.com 的网页会根据需要调用您的类。
'''
from collections import deque
import time
class Order:
    def __init__(self) -> None:
        self.userid
        self.itemid
        self.timestamp

class SellerCalculator:
    def __init__(self,duration) -> None:
        self.q = deque()
        self.count = dict() # key: itemid value: times
        self.duration = duration
    def purchase(self,order:Order):
        if order.itemid in self.count:
            self.count[order.itemid] += 1
        else:
            self.count[order.itemid] = 1
        self.q.append([order.itemid,order.timestamp])

    def GetBestSeller(self,k:int)->list[int]: # return [itemid1,itemid2....]
        self.clear_deque()
        arr = []
        for itemid,times in self.count.items():
            arr.append([itemid,times])
        arr.sort(key = lambda x:x[1],reverse = True)
        result = []
        k = min(len(arr),k)
        for i in range(k):
            result.append(arr[i][0])
        return result

    def clear_deque(self):
        curtime = time.time()
        while len(self.q) > 0 and curtime - self.q[0][1] > self.duration:
            itemid = self.q[0][0]
            self.count[itemid] -= 1
            if self.count[itemid] == 0:
                del self.count[itemid]
            self.q.popleft()
