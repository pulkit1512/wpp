class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def __add__(self,other):
        return self.__salary+other.__salary
    def __sub__(self,other):
        return self.__salary-other.__salary
pulkit=employee("pulkit",10000)
niranjan=employee("niranjan",5000) 
print(pulkit+niranjan)
print(pulkit-niranjan)
print(niranjan+pulkit)  




       