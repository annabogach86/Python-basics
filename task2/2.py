def user_data(name, surname, year_birth, city, email, telephone):
    user_data_dict = {'name': a, 'surname': b, 'year_birth': c, 'city': d, 'email': e, 'telephone': f}
    return user_data_dict
a = input('Name: ')
b = input('Surname: ')
c = input('Year of birth: ')
d = input('City of residence: ')
e = input('email: ')
f = input('Telephone: ')
result = user_data(name=a, surname=b, year_birth=c, city=d, email=e, telephone=f)
print(result)




