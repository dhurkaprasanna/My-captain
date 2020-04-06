li=[]
print("The list is: ")
print(li)
while(True):
        n=int(input("Enter the element to be inserted: "))
        index=int(input("Enter the index: "))
        li.insert(index,n)
        print("The list is: ")
        print(li)
        inp=input("Want to continue insertion in list y/n: ")
        if(inp=="N" or inp=="n"):
            break
t=("a","b","c","d")
print("The tuple is: ")
print(t)
while(True):
        index=int(input("Enter the index to access: "))
        if(index>=4):
            print("Enter index only from 0 to 3")
            continue
        print("The element at index "+str(index)+" is "+str(t[index]))
        inp=input("Want to continue accessing the tuple y/n: ")
        if(inp=="n" or inp=="N"):
              break
d={"a":"apple","b":"Ball","c":"cat","d":"dog"}
print("The dictionary is: ")
print(d)
while(True):
        index=input("Enter the element to be deleted: ")
        if index not in d:
            print("Enter valid element which is present in the dictionary only")
            continue
        print("The dictionary now is:")
        del d[index]
        print(d)
        inp=input("Want to continue deletion in dictionary y/n: ")
        if(inp=="n" or inp=="N"):
            break
print("Thank You")
    

