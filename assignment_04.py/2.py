# t = int(input("enter the number of test cases:"))

# for _ in range(t):
#     num1 = int(input("enter the num1:"))
#     num2 = int(input("enter the num2:"))
#     count=0
#     for i in range(num1, num2 + 1):
        
#         for j in range(1, i + 1):
#             if i == j * j:
#                 count += 1
#     print("count is:",count)

def count_squares_basic(num1, num2):
    count = 0
    for i in range(num1, num2 + 1):
        
         for j in range(1, i + 1):
            if i == j * j:
                 count += 1
    return count

# Read the number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    A, B = map(int, input().strip().split())
    
    print(count_squares_basic(A, B))

'''Here's what each part does:

input(): This function takes input from the user as a string. By default, it reads a line of text (up to the newline character).

.strip(): This method removes any leading and trailing whitespace (including spaces, tabs, and newline characters) 
from the input string. It ensures that there are no extra spaces before or after the actual input values.

.split(): This method splits the input string into a list of substrings based on whitespace. For example,
 if the input string is "3 9", split() will convert it into the list ['3', '9'].

map(int, ...): The map() function applies the int function to each element of the list returned by split(). 
It converts each substring into an integer. So, ['3', '9'] becomes [3, 9].

A, B = ...: This unpacks the list [3, 9] into two variables, A and B, assigning A the value 3 and B the value 9.
   def count_squares_basic(num1, num2):
    count = 0
    i = num1
    while i <= num2:
        j = 1
        while j * j <= i:
            if i == j * j:
                count += 1
            j += 1
        i += 1
    return count
'''