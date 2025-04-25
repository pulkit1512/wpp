def fibbonacci(n):
    if n<=1:
        return n
    return fibbonacci(n-1)+fibbonacci(n-2)
t=int(input("enter the number of test cases:"))
l=[]
for i in range(t):
    n=int(input("enter the number n:"))
    l.append(n)
max=max(l)
# here we make new list and add the fibonacci number until it is greater than the maximum number in the list
# and then we check is the given element of the list is in a new list or not
# if it is in the list then it is a fibonacci number else it is not a fibonacci number
l1=[]
i=0
while(True):
    if(fibbonacci(i)>max):
        break
    else:
        l1.append(fibbonacci(i))
    i=i+1    
for i in range (len(l)):
    n=l[i]
    if n in l1: 
        print("the number",n,"is a fibonacci number")
    else:
        print("the number",n,"is not a fibonacci number")    
                                                                