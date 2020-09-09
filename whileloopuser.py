r="y"
while(r=="y"):
    i=1;
    print("\t\tEnter value")
    x=int(input("x="))
    if(x>=1 and x<=10):
        while(i<=10):
            print("\t\t",x,"*",i,"=",i*x)
            i=i+1;
    else:
        print("\t\tValue not between 1 and 10 ")
    print("\t\tDo you want to continue")
    r=input("\t\tanswer = ")
    
print("\t\tOh,good bye")
