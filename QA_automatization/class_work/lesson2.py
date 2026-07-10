shopping_cart = ['orange', 'peach', 'lemon']
empty_list =[]
mixed_list = [2, 'orange', 3.45, True]
fruits = ['orange', 'peach', 'lemon']
first,second,third = fruits   #unpack but u need to unpack all elements from the list
print(first)
print(second)
print(third)
numbers = [1 ,4 ,6 , 3, 5]
print(sorted(numbers, reverse=True))
names = ['Vovazavodyanny', 'Lenth', 'longest']
print(sorted(names,key=len))
#sort and sorted sorted retuns new collection sort its method of list and he changes list
fruits = ['orange', 'peach', 'lemon', 'orange']
fruits.append('yalla')
print(fruits)
fruits.insert(1, 'pop')
print(fruits)
first_peach_index = fruits.index('peach')
print(first_peach_index)
#remove delete just first time that see in list
fruits.remove('orange')
print(fruits)
#pop can delete from index and pop returns element that u deleted
fruits.pop(2)
print(fruits)
numbers= [10, 20, 30]
deleted = numbers.pop(1)
print(numbers,deleted)

numbers_tuple = (1,2,3,4,5,6,7)
my_tuple = ([1,2,3], ['vova', 'dima'])
first_element = my_tuple[0]
print(first_element)
nested_tuple = (1,2,(3,4),5)
print(nested_tuple[2])
print(nested_tuple[2][1])
print(3 in nested_tuple[2])
print(1 in nested_tuple)

for el in my_tuple:
    print(el)

original_tuple = (5,6,89,34,1,3,6,7,23,4)
sorted_tuple = tuple(sorted(original_tuple))
print(sorted_tuple)
m_string = ''.join(map(str,original_tuple))
print(m_string)

response = {
    'status': 'succses',
    'user' : {'id': 1, 'name' : 'Vova'}
            }

print(response['user']['id'])
print(response['user']['name'])
print(response['status'])
value = 10.01
print(isinstance(value, (int,float)))
print(type(value))
data = [1,2,3,4]
print(isinstance(data, list))

team_ages = {
    'Alex':23,
    'Viki':42,
    'Petr':52,
    'Den':32,
    'Olga':26
}
print(team_ages.keys())
print(team_ages.values())

team_names = ['Alex','Viki', 'Petr', 'Den', 'Olga']
team_numbers = [12, 33, 44, 55, 66]
team_ages = {name:age for name, age in zip(team_names,team_numbers)}
print(team_ages)