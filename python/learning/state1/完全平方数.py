n=1
while(n*n-(n-1)*(n-1))<=168:        #判断上限
    n+=1
for i in range(1,85**2):
    a=i**0.5               
    b=a%1                           #开根号的小数位为0
    m=i+168
    n=m**0.5
    q=n%1                           #开根号的小数位为0
    if b==0 and q==0:
        print(i-100)                 #输出结果
    


