'''
带有默认值的dict
如果defaultdict的value存储int类型，那么value的默认值就是0
如果defaultdict的value存储string类型，那么value的默认值就是空字符“”

普通的dict如果要取出一个key不存在的value，就会直接报错
但是defaultdict不会，他会直接返回一个默认值
'''

from collections import defaultdict

def defaultInt():
    '''
    默认值是int 0
    '''
    # 创建一个 defaultdict，指定默认值类型为 int
    d = defaultdict(int)
    # 访问不存在的键 'a'，默认值类型为 int，默认值为 0
    print(d['a'])  # 输出：0

    d['a'] += 1
    print(d['a']) # 输出： 1

def defaultString():
    '''
    默认值是string ""
    '''
    d = defaultdict(str)
    print(d['a'])  # 输出：0

    d['a'] = "Hello World!"
    print(d['a'])

def defaultList():
    '''
    默认值是list []
    '''
    d = defaultdict(list)
    print(d['a'])  # 输出：0

    d['a'].append('Hello World!')
    d['a'].append('Hello')
    d['a'].append('World!')
    print(d['a'])
if __name__ == '__main__':
    defaultInt()
    defaultString()
    defaultList()