class Member:
    no_of_leaves=9
    def __init__(self,a,b,c,):
        self.name=a
        self.age=b
        self.salary=c
    def identity(self):
        return  f"the name is{self.name} age is {self.age} salary is {self.salary}"
    @classmethod
    def from_dash(cls,string):
        y= string.split('-')

        return cls(y[0],y[1],y[2])
    @staticmethod
    def printgood(stri):
        print (f"this is good {stri}")


class Player(Member) :
    no_of_leaves = 80
    def __init__(self,a,b,c,d):
         self.name = a
         self.age = b
         self.salary = c
         self.huda=d


    def bugichuki(self):
        return f"the salary is{self.salary} age is {self.age} name is {self.name}"
class Cooler(Player):

    languag=9
    def knownlangu(self):
        return f"he knows {self.languag}"

kaarn=Member.from_dash('Karar-23-2445')
inan=Member('INAN',21,2234556)
saraf=Member('SARAF',12,23345)
hasan=Player('HASAM',32,234,1)
nymur=Cooler('nym',21,2334,2)
print(nymur.no_of_leaves)
