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

