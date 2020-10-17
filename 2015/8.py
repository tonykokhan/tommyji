class People:
    country = 'China'

    @staticmethod
    def getCountry():
        return People.country


print(People.getCountry())
