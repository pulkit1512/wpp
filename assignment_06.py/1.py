class password_manager:
    def __init__(self,old_password):
        self.old_password=[]
        self.old_password.append(old_password)
    def get_password(self):
        return self.old_password[-1]
    def set_password(self,new_password):
        self.new_password=new_password# this is attribute
        if new_password not in self.old_password:
            self.old_password.append(new_password)
            return "Password added successfully"
        else:
            return "Password already has taken"
    def is_correct(self,password):
        self.password=password
        if password in self.old_password[-1]:
            return True
        else:
            return False
password=password_manager("1234")
password.set_password("pulkit@151206")
print(password.get_password())
print(password.set_password("pulkit@15122006"))
print(password.is_correct("1234"))
