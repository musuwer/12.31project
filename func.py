def func(a,b):
    return a+b
a,b=map(int,input().split())
print(func(a,b))
for i in range(1,a+b):
# <<<<<<< Updated upstream
# <<<<<<< Updated upstream
# <<<<<<< Updated upstream
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
# =======
#     print(i)
# >>>>>>> Stashed changes
#     print(i)
# >>>>>>> Stashed changes
# =======
#     print(i)
# >>>>>>> Stashed changes
x=12
if x >10:
    pass
# =======
d = dir(math)
for i in range(0, len(d), 8): #递归地打印列表中的元素，并按每行8个元素的格式进行输出
    print('\t'.join(d[i:i+8]))