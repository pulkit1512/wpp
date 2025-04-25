t=int(input("enter the number of test cases:"))

for i in range(t):
    str=input("enter the string:")
    a=str.split()
    print(a)  
    for i in range(len(a)):
        oper=0
        b=a[i]
        start=0
        end=len(b)-1
        while(start<end):
           
           oper=oper+abs(ord(b[start])-ord(b[end]))
           #The abs() function takes the absolute value of the difference.
           #  This ensures that the result is always non-negative,
           #  regardless of the order of the characters.
           start=start+1
           end=end-1
        print(oper)   

#code to print the ascii value of the character
# ## Get a character from the user
# char = input("Enter a character: ")

# # Convert the character to its ASCII value
# ascii_value = ord(char)

# print(f"The ASCII value of '{char}' is {ascii_value}.")
