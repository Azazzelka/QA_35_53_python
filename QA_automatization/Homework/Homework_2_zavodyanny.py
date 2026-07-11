def print_list_reverse(lst:list):
    if lst is None or not isinstance(lst,list) or lst == []:
        return print('wrong list')
    return print(lst[::-1])

print_list_reverse([1, 2, 3, 4, 5])
print_list_reverse([])
print_list_reverse([True, False])
print_list_reverse(['asda', 'asf'])

print('*******************************')

def is_valid_point(tup:tuple):
    if tup is None or tup == ():
        return None
    if not isinstance(tup,tuple) or len(tup)>2 or not all(isinstance(el, (int,float)) for el in tup):
        return False
    return True

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5"))) # False
print(is_valid_point([3, 5])) # False
print(is_valid_point((1, 2, 3))) # False
print(is_valid_point(())) # None
print(is_valid_point(None)) # None

print('*************************')

def print_sublist_reverse(lst,start,finish):
    if (lst is None
        or lst == []
        or not isinstance(lst, list)
        or not isinstance(start, int)
        or not isinstance(finish, int)
        or start < 0
        or finish < 0
        or start >= len(lst)
        or finish >= len(lst)
        or start > finish
    ):
        return 'Wrong Args'
    new_lst = lst[:]
    new_lst[start:finish+1] = new_lst[start:finish+1][::-1]
    return new_lst


print(print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3))
print(print_sublist_reverse([1,2,3,4,5,6,7,8,9,10],10, 11))

print('***********************')

def get_students_by_grade(students):
    empty_dict = {}
    if students is None or students == 0 or students == {} or not isinstance(students, dict):
        return empty_dict
    for student, grade in students.items():
        empty_dict.setdefault(grade, []).append(student)
    return empty_dict

def get_students_by_grade2(students):
    empty_dict = {}
    if students is None or students == 0 or students == {} or not isinstance(students, dict):
        return empty_dict
    for student, grade in students.items():
        if grade not in empty_dict:
            empty_dict[grade] = []
        empty_dict[grade].append(student)
    return empty_dict

test_list1 = {"Vova": 70,
    "Dima": 94,
    "Nikita": 94,
    "Kristina":70,
    "Vasiliy":70,
    "Aleksey":30}

test_list2 = None
print(get_students_by_grade(test_list1))
print(get_students_by_grade(test_list2))

print(get_students_by_grade2(test_list1))
