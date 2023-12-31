
def func(a,b):
    return a+b
a,b=map(int,input().split())
print(func(a,b))
for i in range(1,a+b+2):
    print(i)
class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func2(self):
        print(f'名字是{self.name}，年龄是{self.age}')
stu=student('musuwer',18)
stu.func2()
