
def func(a,b):
    return a+b
a,b=map(int,input().split())
print(func(a,b))
for i in range(1,a+b):
    print(i)
for i in range(1,a+b+2):
    print(i)
while True:
    n=1
    if n >10:
        break
    else:
        n+=1

class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func2(self):
        print(f'名字是{self.name}，年龄是{self.age}')
stu=student('musuwer',18)
stu.func2()
