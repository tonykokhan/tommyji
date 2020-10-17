class People:
    country = 'China'

    @classmethod
    def getCountry(cls):
        return cls.country

    @classmethod
    def setCountry(cls, country):
        cls.country = country


p = People()
print(p.getCountry())  # China
print(People.getCountry())  # China

p.setCountry('Japan')
print(p.getCountry())
print(People.getCountry())

p.setCountry('Indian')
print(p.setCountry('Indian'))  # None
print(p.getCountry())
print(People.getCountry())
