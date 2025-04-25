t=int(input("enter the number of test cases:"))
l=[]
for i in range(t):
    str1=input("enter the string:")
    l.append(str1)
for i in range(t):
    str1=l[i]
    for j in range(len(str1)):
        end=str1[len(str1)-j-1]
        start=str1[len(str1)-j-2]
        if(ord(end)>ord(start)):
            end,end=start,end
            print(str1) 
        elif(ord(end)==ord(start)):
            print("no answer")
            break
        