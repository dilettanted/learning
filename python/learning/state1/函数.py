print()
'''#幂函数
def power(x,y):
    i=0
    j=1
    while i<y:
        i+=1
        j=j*x
    return j


m=int(input('please enter the number "x":'))
n=int(input('please enter the number "y":'))
print(power(m,n))
'''


print()
'''#最大公约数
def gcd(x,y):
    i=0
    j=[]
    k=0
    if x>y:
        x,y=y,x
    for i in range(1,y):
        if x%i==0 and y%i==0:
            j.append(i)
    k=max(j)
    return k


m=int(input('please enter first number:'))
n=int(input('please enter second number:'))
print(gcd(m,n))
'''

