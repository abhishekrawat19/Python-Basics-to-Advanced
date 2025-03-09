class Highschool:
    def __init__(self,name,grade,percenatage):
        self.name=name
        self.grade=grade
        self.percentage=percenatage

    def display(self):
        print(self.name,self.grade,self.percentage)
    
class school(Highschool):
    def __init__(self,name,grade,percenatage,nameS,gradeS,YOPS):
        super().__init__(name,grade,percenatage)
        self.nameS=nameS
        self.gradeS=gradeS
        self.YOPS=YOPS
    
    def display(self):
        super().display()
        print(self.nameS,self.gradeS,self.YOPS)
    

    
class college(school):
    def __init__(self,name,grade,percenatage,nameS,gradeS,YOPS,nameC,gradeC,YOPC):
        super().__init__(name,grade,percenatage,nameS,gradeS,YOPS)
        self.nameC=nameC
        self.gradeC=gradeC
        self.YOPC=YOPC

    def display(self):
        super().display()
        print(self.nameC,self.gradeC,self.YOPC)
    
    

abhi=college("GMPS",8.5,85,"GMPS",9.5,2021,"AKTU",7,2025)
abhi.display()



