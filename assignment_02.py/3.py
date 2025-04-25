T = int(input("Enter no. of testcases: "))
l = []

for i in range(T):
    n = int(input())
    l.append(n)

for i in range(T):
    count = 0
    n = l[i]
    for j in range(len(str(n))):
        if int(n[j]) == 0: continue
        if n%int(n[j])==0:
            count += 1
    print(count)

