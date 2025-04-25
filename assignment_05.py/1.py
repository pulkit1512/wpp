t=int(input("enter the number of test cases:"))
l=[]
for i in range(t):
    num1=int(input("enter the number num1:"))
    num2=int(input("enter the number num2:"))
    my_tupple=(num1,num2)
    
    l.append(my_tupple)
l1=[]
for i in range(t):
    n=l[i]
   
    for j in n:
        for k in range(n[0],n[1]+1):
            xor=j^k
            l1.append(xor)
max=max(l1)
print(max)
        

    