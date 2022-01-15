U=float(input("Enter any natural number: "))
b=0
c=1
if(U%1==0 and U>0):
    while(U//c>=1):
        b+=1
        c=c*10
    print("The total number of digit is: ",b)
else:print("This is not a natural number.")
        
