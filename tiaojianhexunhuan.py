x=int(input("please enter an interger:"))
if x<0:
    x=0
    print("Negative changed to zero")
elif x==0:
    print("Zero")
else:
    print("More")
    #Loops List
    a=['cat','window','defenestrate']
    for x in a:
        print(x,len(x))