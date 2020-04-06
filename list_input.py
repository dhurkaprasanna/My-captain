
l1=[12,-7,5,64,-14]
print("Input: list1= [12,-7,5,64,-14]")
print("Output: ",end="")
j=0
n=len(l1)
for i in l1:
    if(i>0):
        if(j==n-1):
            print(i,end="")
        else:
            print(i,end=",")
    j+=1
print()
l2=[12,14,-95,3]
print("Input: list2= [12,-7,5,64,-14]")
print("Output: ",end="")
j=0
n=len(l2)
for i in l2:
    if(i>0):
        if(j==n-1):
            print(i,end="")
        else:
            print(i,end=",")
    j+=1

print()
print("For custom input ")
n=int(input("Enter the number of items in the list: "))
list1=[]
print("Enter the items: ")
i=0
while(i<n):
    list1.append(int(input()))
    i+=1
print("Output: ",end="")
i=0
j=0
while(i<n):
    if(list1[i]>0):
        if(j==0):
            print(list1[i],end="")
        else:
            print(",",end="")
            print(list1[i],end="")
    j+=1
    i+=1
