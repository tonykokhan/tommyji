class People:
    country = 'China'

    @classmethod
    def getCountry(cls):
        return cls.country

    @classmethod
    def setCountry(cls, country):
        cls.country = country


p = People()
print(p.getCountry())
print(People.getCountry())

p.setCountry('Japan')
print(p.getCountry())
print(People.getCountry())

p.setCountry('American')
print(p.getCountry())
print(People.getCountry())
