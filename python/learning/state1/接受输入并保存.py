def file_write():
    file_name=input('请输入文件名称：')
    file=open(file_name,'a')
    print('请输入文件内容：【单独输入 \':w\'保存并退出】')
    while True: 
        file_content=input()
        file=open(file_name,'a')
        if file_content==':w':
            file.close()
            break
        else:
            file.write(file_content)
            file.close()



file_write()