
score=int(input('请输入你的成绩：'))
level=['D','C','B','A','S']
if score<60:
    print(level[0])
elif score<80:
    print(level[1])
elif score<90:
    print(level[2])
elif score<100:
    print(level[3])
else:
    print(level[4])