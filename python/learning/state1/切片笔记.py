
#one:
list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]   #切片
print(list1)

#two:
list1 = []                                                          #切片（效果同上）
for x in range(10):
    for y in range(10):
        if x%2 == 0:
            if y%2 != 0:
                list1.append((x, y))

#three:
list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]                     #替换
list1[1][2][0] = '小鱿鱼'

#four
list2 = list1.copy()                                              #复制

list2.clear()                                                     #清空

#five:
list1=['1.just do it' ,'2.一切皆有可能','3.让编程改变世界','4.impossible is nothing']
list2=['4.阿迪达斯','3.李宁','2.鱼c工作室','1.耐克']
list3 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]

