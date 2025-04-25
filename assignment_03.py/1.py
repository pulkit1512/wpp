# digital root of a number
def digital_root(n):
    sum=0
    for i in range(len(str(n))):
        r=n%10
        sum=sum+r
        n=n//10
    return digital_root(sum) if sum>9 else sum

n=int(input("Enter the number n:"))
print("The digital root of the number is:",digital_root(n))
