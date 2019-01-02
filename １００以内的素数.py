for i in range(2,101):
    j=2
    while j<=i:
        if i%j==0:
            break
        j+=1
    if j<i:
        continue
    else:
        print(i,end=" ")