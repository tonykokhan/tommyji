class People:
    country = 'China'


print(People.country)
p = People()
print(p.country)
p.country = 'Japan'
print(p.country)
print(People.country)
del p.country
print(p.country)
