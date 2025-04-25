def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def is_fibonacci(num):
    a, b = 0, 1
    #this while loop will run till the value of b is less than or equal to the value of num
    #
    while b <= num:
        if b == num:
           return True
        a, b = b, a + b
         
    else:
        return False


t = int(input("Enter the number of test cases: "))
numbers = [int(input("Enter the number n: ")) for _ in range(t)]
    
for n in numbers:
    if is_fibonacci(n):
        print(f"The number {n} is a Fibonacci number.")
    else:
        print(f"The number {n} is not a Fibonacci number.")


