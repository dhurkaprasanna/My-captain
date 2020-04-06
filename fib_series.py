num1=0
num2=1
n=int(input("Enter the value of n: "))
print("The first "+str(n)+" fibonacci numbers are:")
if n==1:
    print(num1,end=" ")
elif n==2:
    print(num1,end=" ")
    print(num2,end=" ")
else:
    print(num1,end=" ")
    print(num2,end=" ")
    n-=2
    while(n>0):
        num3=num1+num2
        num1=num2
        num2=num3
        print(num2,end=" ")
        n-=1
    
    
