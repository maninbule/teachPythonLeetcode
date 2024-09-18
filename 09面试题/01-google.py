'''
给你一个文件夹的目录
每一个文件下面可能会多个子文件夹
每一个子文件夹也可能有多个子文件夹
返回所有与自己的父文件(层次不一定为1)夹同名的文件夹名字

文件夹有：
1. id int
2. name str
3. list(表示子文件夹的指针) list[int] 每一个int是一个id
'''
from collections import defaultdict
class folder:
    def __init__(self,id:int,name:str,children:list):
        self.id = id
        self.name = name
        self.children = children
def findSameNamefolder(folder:folder)->list[folder]:
    count = defaultdict(int)
    return dfs(folder,count)

def dfs(folder:folder,count:defaultdict)->list[folder]:
    ans = []
    if count[folder.name] >= 1:
        ans.append(folder)
    count[folder.name] += 1
    for child in folder.children:
        ans += dfs(child,count)
    count[folder.name] -= 1
    return ans




