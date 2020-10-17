class People:
    country = 'China'

    @classmethod
    def getCountry(cls):
        return cls.country


p = People()
print(p.getCountry())
print(People.getCountry())
