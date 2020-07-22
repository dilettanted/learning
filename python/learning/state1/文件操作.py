print()
file=open('D:\\files\\fdm\\music\\openme.mp3')
for each in file:
    file2=open('D:\\files\\fdm\\music\\openme1.txt','a')
    print(each)
    file2.write(each)
    file2.close()
file.close()


'''

file1=open('D:\\files\\fdm\\music\\openme.mp3')
file2=open("D:\\files\\fdm\\music\\openme.txt","a")
file2.write(file1.read())
file1.close()
file2.close()

'''