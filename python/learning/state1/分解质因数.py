number=int(input('请输入一个整数:'))
list=[]
num=number
for each in range(2,number):
    if num%each==0 and num>0:
        list.append(each)
        num=num/each
for i in list:
    print(i,end=' ')

    #失败