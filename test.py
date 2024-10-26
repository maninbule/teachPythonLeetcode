


'''
利用二分查找找到最小的 k
，并验证在给定的 k 下，是否能够用不超过 d 个送餐员处理完所有订单。
验证的方法是遍历 orders，计算需要的送餐员数量。

具体步骤：

初始化 left 为 1（最小可能的订单数），right 为 max(orders)（最大可能的订单数）。
当 left 小于 right 时：
计算 mid 为 (left + right) // 2，表示当前尝试的每个送餐员的最大订单数。
调用辅助函数 check(k) 来判断 k 是否足够小，使得在 d 个送餐员的情况下能够处理所有订单。
如果 check(k) 返回 True，说明 k 可以更小，因此设置 right = mid。
否则，设置 left = mid + 1。
最后返回 left，即为所求的最小 k。

time:O(nlog(maxvalue)) n就是元素个数， log(maxvalue)二分的是1-maxvalue
sapce:O(1)

对于给定的 k，我们遍历 orders，用送餐员从两个相邻餐厅中尽可能多地获取订单。
在遍历过程中，尽量把当前餐厅的订单和下一个餐厅的订单合并，查看是否可以让当前的 k 处理这些订单。如果可以，计数一个送餐员。

贪心的思路
优先组合相邻餐厅订单：

当送餐员可以从两个相邻的餐厅取订单时，check 函数会尝试将当前餐厅和下一个餐厅的订单相加，看是否能够不超过 k。
如果两者相加不超过 k，那么就用一个送餐员处理这两个餐厅的订单。这是一种贪心选择，因为这样做可以最大限度地减少送餐员的数量。
这种贪心选择的核心在于：在当前局部选择中，优先合并订单总和不超过 k 的相邻餐厅，期望通过局部最优解达到全局最优解。

一个餐馆
同时拿2个餐馆的条件是什么？
'''

def solution(orders, d):
    # Helper function to determine if given k can handle all orders with d dashers
    def check(k):
        required_dashers = 0
        i = 0
        pre = 0
        while i < len(orders):
            cur = orders[i] + pre
            required_dashers += (cur + k-1) // k
            if cur % k != 0:
                pre = k - cur % k
            i += 1
            # If we already need more dashers than available, return False early
            if required_dashers > d:
                return False
        return True

    # Initialize binary search range
    left, right = 1, max(orders)
    res = right
    # Binary search for the minimum capacity k
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            res = mid
            right = mid -1 # Try smaller values of k
        else:
            left = mid + 1  # Increase k
    return res
# 只改了check函数

# # 测试用例
# orders1 = [3, 6, 7, 11]
# d1 = 8
# print(min_capacity(orders1, d1))  # 输出：4

# orders2 = [30, 11, 23, 4, 20]
# d2 = 5
# print(min_capacity(orders2, d2))  # 输出：30

orders2 = [3,3,7,9]
d2 = 8
# [1,1,3,4]
print(solution(orders2, d2))  # 输出：30
# 好，我先下了