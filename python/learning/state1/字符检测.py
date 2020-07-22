#错误

list1=['qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']
list3=['1234567890']
list4=[r'~!@#$%^&*()_+=-`:"{}|:\"<>?,./;']
def fin(x):
    i=0
    j=0
    k=0
    v=0
    a=0
    while a<(len(x)-1):
        for each in x[a]:
            if each in list1:
                i+=1
            elif each in list3:
                j+=1
            elif each in list4:
                k+=1
            else:
                v+=1
            print('第%d个字符串共有：英文字母%d个，数字%d个，空格%d个，其他字符%d个'%(a,i,j,v,k))
        a+=1
sen=input('请输入字符串：')
print(fin(sen))