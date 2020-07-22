def product(*numbers):
    if numbers!=0:
        sum=1
        numbers=input("请输入两个及以上的数字:")
        int(numbers)
        for n in numbers:
            sum=sum*n
    return sum



