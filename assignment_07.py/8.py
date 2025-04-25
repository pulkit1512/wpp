class message:
    def __init__(self,message):
        self.message=message
    def decode(self):
      
       dict={i:j for i in range(1,27) for j in "abcdefghijklmnopqrstuvwxyz"}
       l=[]
       for k in self.meassage:
           l.append(k)
       for h in l:
           b=dict.get(h)
       return b    
m1=message("1123")
print(m1.decode)     
