#find smallest num in list
#find largest num in list
#find avg num
#concat all these three values
class lists:
    def __init__(self):
        self.mini=999
        self.maxi=0
    def list(self,number):
        for num in number:
            while num<self.mini:
                self.mini=num#1
            break
            while num>self.maxi:
                self.maxi=num#6
            break
    def average(self,number):
        avg=sum(number)/len(number)
        return int(avg)
display=lists()
number=list(map(int,input().split()))
display.list(number)
res=str(display.mini)+str(display.maxi)+str(display.average(number))
print(res)
    
    
