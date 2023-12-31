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
for i in range(0, len(d), 8): #递归地打印列表中的元素，并按每行8个元素的格式进行输出
    print('\t'.join(d[i:i+8]))