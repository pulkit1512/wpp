T = int(input("Enter testcases: "))
l = [chr(x) for x in range(97, 123)]
#list comprerhension

for i in range(T):
    s = input("Enter the string: ").lower()
    isPangram = True
    for i in range(len(l)):
# firstly it search for the value of a and trhen for the b ans so on       
        if l[i] not in s:
            isPangram = False
            break
# is pangram ia s bollean value so if the value is true then it will print isPangram        

    if isPangram: print("isPangram")
    else: print("isNotPangram")

