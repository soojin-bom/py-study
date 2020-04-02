a=1
b=2
c=3
s=a+b+c
r=s/3
print(r)

'''
def average():
    a=1
    b=2
    c=3
    s=a+b+c
    r=s/3
    print(r)
average()
'''

'''
#input에 관한 함수
#a,b,c는 매개변수. parameter
def average(a,b,c):
    s=a+b+c
    r=s/3
    print(r)

#10, 20, 30은 인자, 즉 argument
average(10,20,30)
'''

#하나의 함수에는 하나의 기능만 갖고있는 것이 좋다.
def average(a,b,c):
    s=a+b+c
    r=s/3
    return r

print(average(10,20,30))

def a():
    return 'haha'
print(a())