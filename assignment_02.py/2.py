d={}
n=int(input("enter the number n:"))
for i in range(1,n):
    product=input("enter product name:")
    price=input("enter price of product in $:")
    d.update({product:price}) 
print(d)   
n=int(input("enter the number n:"))
for i in range(1,n):
 product_name=input("enter the product name customer needed:")
 if(product_name in d):
    print(price)
 else:
    print("this product is not in our dictionary:")





