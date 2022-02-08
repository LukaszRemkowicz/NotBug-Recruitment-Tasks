"""

• Create good script to create new list, which only contains users from Poland. Try to do it  with List Comprehension.
users = [{"name": "Kamil", "country":"Poland", {"name":"John", "country": "USA"}, {"name":  "Yeti"}]

"""

users = [{"name": "Kamil", "country": "Poland"}, {"name": "John", "country": "USA"}, {"name": "Yeti"}]
users_from_poland = [user for user in users if 'country' in user and user['country'] == 'Poland']

"""

• Display sum of first ten elements starting from element 5:  
numbers = [1,5,2,3,1,4,1,23,12,2,3,1,2,31,23,1,2,3,1,23,1,2,3,123] 

"""

numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]
print(sum(numbers[5:15]))

"""

• Fill list with powers of 2, n [1..20]

"""

result = [num**2 for num in range(1, 21)]


import requests

a = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100&offset=200')
print(a.__dict__)