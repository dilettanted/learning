i=1
while i<10:
    j=1
    while j<=i:
        k=i*j
        print('%d*%d=%d'%(i,j,k),end=' ')           
        j+=1
    i+=1
    print()