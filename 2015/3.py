class People:
    name = 'jack'
    age = 12

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


p = People()
print(p.getName(), p.getAge())
