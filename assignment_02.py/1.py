word=input("enter the word")
result=""
for i in range(0,len(word)):
    if(i%2==0):
        result+=word[i].upper()

    else:
      result+=word[i].lower()
print(result)       




