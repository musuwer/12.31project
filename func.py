import math
def func(a,b):
    return a+b
a,b=map(int,input().split())
print(func(a,b))
for i in range(1,a+b+2):
    print(i)
while True:
    n=1
    if n >10:
        break
    else:
        n+=1
d = dir(math)
# 递归地打印列表中的元素，并按每行8个元素的格式进行输出
for i in range(0, len(d), 8):
    '''
    range(0, len(d), 8)是一个Python的内置函数range()的用法，
    它会生成一个以0开始，以len(d)结束（不包含len(d)），
    步长为8的整数序列
    '''
    print('\t'.join(d[i:i+8]))
