name=input('请输入句子：')
l=list(name)
i=l.copy()
l.reverse()
if i==l:
    print('是回文联！')
else:
    print('不是回文联！')