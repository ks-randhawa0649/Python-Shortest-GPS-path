Fname=input("File Name:")
F=open(Fname,"r")
la_arr = []
lo_arr = []
time_arr = []

for l in F.readlines():

    L=l.split(";")
    la_arr.append(L[0])
    lo_arr.append(L[1])
    time_arr.append(L[4])
l=len(la_arr)
print("x=",l)
    

F.close()    
