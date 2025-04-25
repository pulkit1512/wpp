t=int(input("teh number of the test cases:"))
l=[]
for i in range(t):
    n=int(input("enter the number :"))
    l.append(n)
for i in range(t):
    n=l[i]
    b=n//2
    a=n-b
    print("the maximum number of pieces can be obtained is",a*b)     