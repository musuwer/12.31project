def func(a,b):
    return a+b
a,b=map(int,input().split())
print(func(a,b))
for i in range(1,a+b+2):
    print(i)