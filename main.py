class Person:
    name = "Sakib"
    occupation = "Python Developer"
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
a.name = "Samiul"

b.name = "Sharika"
b.occupation = "Data Analyst"
# a.occupation = "Web Developer"
a.info()
b.info()

# Constructors

class Person():
    
    def __init__(self, n, o):
        # print("Hey I am a person")
        self.name = n
        self.occ = o
    
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Samiul", "Web Developer")
b = Person("Sharika", "Data Analyst")

a.info()
b.info()