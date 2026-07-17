def create_profile(name,age=18,city='Unknown'):
    return {
        "name": name,
        'age': age,
        'city': city
    }

print(create_profile('Anna'))
print(create_profile("Tom", 25))
print(create_profile(city="Haifa", name="Maria"))

def sum_even_numbers(*args):
    result = 0
    for arg in args:
        if arg % 2 == 0:
            result += arg
    return result

print(sum_even_numbers(1, 2, 3, 4, 5, 6)) # 12
print(sum_even_numbers(7, 9)) # 0
print(sum_even_numbers()) # 0

def sum_even_numbers2(*args):
    return sum(arg for arg in args if arg % 2 == 0)

print(sum_even_numbers2(1, 2, 3, 4, 5, 6)) # 12
print(sum_even_numbers2(7, 9)) # 0
print(sum_even_numbers2()) # 0


def print_pet_info(name, **info):
    result = f'Name:{name}\n'
    if not info:
        result += 'No additional information'
    for key, val in info.items():
        result+= f'{key} = {val}\n'
    return result

print(print_pet_info(
"Lucky",
age=4,
color="White",
breed="Spitz"))

print(print_pet_info('lucky'))

def merge_lists(*lists):
    result = []
    for lst in lists:
        result += lst
    return result

print(merge_lists([1, 2],[3],[4, 5],[]))

def build_message(*words, separator=""):
    if separator == '':
        separator = ' '
    return separator.join(words)


print(build_message('2026', '07', '15', separator='-'))