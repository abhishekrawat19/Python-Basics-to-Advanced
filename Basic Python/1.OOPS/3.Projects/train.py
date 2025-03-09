

class Passenger:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def display(self):
        print(self.name,self.age,self.gender)
    
class Boarding(Passenger):
    def __init__(self,name,age,gender,timimg,platform,date):
        super().__init__(name,age,gender)
        self.timing=timimg
        self.platform=platform
        self.date=date
    
    def display(self):
        super().display()
        print(self.timing,self.platform,self.date)
    

    
class Confirmation(Boarding):
    def __init__(self,name,age,gender,timimg,platform,date,seatno,confirm):
        super().__init__(name,age,gender,timimg,platform,date)
        self.seatno=seatno
        self.confirm=confirm

    def display(self):
        super().display()
        print(self.seatno,self.confirm)
    
    
abhi=Confirmation("Abhi",23,"male","10:00 AM","Platform 2","22/03/2025","B-34",True)
abhi.display()
