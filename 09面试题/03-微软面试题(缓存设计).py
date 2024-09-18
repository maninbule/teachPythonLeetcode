'''
让你设计一个class

class主要让你模拟一个缓存
功能：
    1. 可以根据资源id，去产生一个url
    2. 可以根据url去访问资源(没有命中的时候，去服务器查询)
    3. 根据url访问资源的时候，首先去缓存里面看是否可以命中(是去看能不能在缓存中查到)
        1) 如果命中了
        2) 如果没有命中，就需要去通过url去获取资源，再放入缓存中
        需要把这个资源设置为缓存最新访问的
        输出是资源
    4. 提供一个打印函数，可以输出这个缓存里面的内容
思路： 就是设计LRU缓存

整体思路：
    存储部分： 使用list来存储访问资源的顺序
             使用dict来存储url和data的对应关系
    缓存设计：
            每次访问url的时候，会把这个资源放在list的最后面，表示最近访问的url(list末尾)
            如果缓存满了的话，就会删除最近没有被使用的url(删除list的第一个)
'''

class Cache:
    def __init__(self,cache_size:int):
        self.urlCache = [] # 只存url
        self.data = dict() # 存储缓存里面每一个url对应的data
        self.cache_size = cache_size
    def getUrlById(self,id:int):
        return f"http://www.abc.com/data/{id}"
    def getDataByUrl(self,url:str)->str:
        # 直接查询，不通过缓存
        return "data of " + url
    # time: O(n)
    def getDataFromCache(self,id:int)->str:
        url = self.getUrlById(id)
        # 命中的情况下
        if url in self.data:
            self.urlCache.remove(url)
            self.urlCache.append(url)
            return self.data[url]
        # 没有命中，我们就需要调用函数去获取资源，然后放入缓存
        dat = self.getDataByUrl(url)
        # 现在要放入资源到缓存，先要查询缓存是否满了
        if len(self.urlCache) == self.cache_size:
            # O(n)
            delurl = self.urlCache.pop(0) # 把最近最少访问的资源给删除了
            del self.data[delurl]
        # 现在缓存肯定不满，就放入资源
        self.urlCache.append(url)
        self.data[url] = dat
        return dat
    def printCache(self):
        for url in self.urlCache:
            print(url)

if __name__ == '__main__':
    cache = Cache(3)
    cache.getDataFromCache(1) # 缓存为[],没有命中，就加载资源1，放入缓存
    cache.getDataFromCache(2)  # 缓存为[1],没有命中，就加载资源2，放入缓存
    cache.getDataFromCache(3)  # 缓存为[1,2],没有命中，就加载资源3，放入缓存
    cache.getDataFromCache(4) # 缓存为[1,2,3],没有命中，就加载资源4，放入缓存
    #cache.printCache() # [2,3,4]
    cache.getDataFromCache(3)
    cache.printCache()  # [2,4,3]

