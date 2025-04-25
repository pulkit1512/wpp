t=int(input("enter the number of test cases:"))
height=1
l=[]
for i in range(t):
    n=int(input("enter the number n:"))
    l.append(n)
for i in range(t):
    n=l[i]
    for j in range(1, n+1):
        if j%2==0:
            height=height+1
        else:
            height=height*2
    print("the height of the tree is:",height)
    height=1




