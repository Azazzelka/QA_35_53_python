
def get_list_element(items,index):
    if not isinstance(index, int):
        raise TypeError('Please enter index data correct Value : int')
    if index >= len(items) or index < 0:
        raise IndexError(f'index is out of range, index range 0 - {len(items)-1}')
    return items[index]

numbers = [10, 20, 30]
try:
    print(get_list_element(numbers, 1))
except (TypeError,IndexError) as e:
    print(e)

try:
    print(get_list_element(numbers, 10))
except (TypeError,IndexError) as e:
    print(e)

def get_user_data(user,key):
    try:
        return user[key]
    except KeyError:
        return 'Key was not found'

user = {
"name": "Anna",
"age": 30
}
print(get_user_data(user, "name"))
print(get_user_data(user, "email"))

def calculate(first_value,second_value):
    return (first_value + second_value)/2

def pars_numbers(f,s):
    first = float(f)
    second = float(s)
    return calculate(first,second)

def calculate_average(first_value,second_value):
    try:
        result = pars_numbers(first_value,second_value)
        print(f'{result}')
    except (ValueError, TypeError) as e:
        print(e)

calculate_average(10,2)
calculate_average('qq', '15')
calculate_average('4','12')
calculate_average(4.2,12)
calculate_average('4,2', 12)

def read_number():
    try:
        num = int(input('Enter your number'))
        print('Number was entered successfully')
    except ValueError as e:
        print(f'Invalid number, {e}')
    finally:
        print('Program finished')

read_number()


def validate_age(age):
    if age < 0:
        raise ValueError('Age can not be negative')
    if age > 120:
        raise ValueError('Age is not realistic')

try:
    validate_age(121)
except ValueError as e:
    print(e)

try:
    validate_age(-1)
except ValueError as e:
    print(e)





