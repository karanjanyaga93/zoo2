class Lion:
    def __init__(self,kingdom,sex,genus):
        self.kingdom=kingdom
        self.sex=sex
        self.genus=genus
    def getKingdom(self):
        return self.kingdom
    def getSex(self) :  
        return self.sex
    def getGenus(self) :
        return self.genus
lion1=Lion("cat","male"," carnivore") 
lion1.getKingdom()
lion1.getSex()
lion1.getGenus()
print(lion1.getKingdom())  
print(lion1.getSex())
print(lion1.getGenus())
