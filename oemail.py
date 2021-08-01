class Employee:
    def __init__(self, a, b):
        self.fname = a
        self.lname = b

    def Explain(self):
        return f"the employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None and self.lname == None:
            return 'set in the setter'
        return f"{self.fname}{self.lname}@inan.com"

    @email.setter
    def email(self, string):
        names = string.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


hindustani_bhau = Employee('HINDUSTANI', 'BHAU')

# hindustani_bhau.fname='US'
# print(hindustani_bhau.email)
# hindustani_bhauemailhindustani_bhau.email='ding.dong@inan.com'
print(hindustani_bhau.email)
hindustani_bhau.fname = 'us'
print(hindustani_bhau.email)
hindustani_bhau.email = 'ding.dong@inan.com'
print(hindustani_bhau.email)
del hindustani_bhau.email
print(hindustani_bhau.email)
hindustani_bhau.email = 'Ar.inan@pappa.com'
print(hindustani_bhau.email)