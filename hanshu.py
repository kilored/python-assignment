def sum(a,b):
    return a+b
func=sum
r=func(5,6)
print (r)
#提供默认值
def add(a,b=2):
    return a+b
r=add(1)
print(r)
r=add(1,5)
print(r)