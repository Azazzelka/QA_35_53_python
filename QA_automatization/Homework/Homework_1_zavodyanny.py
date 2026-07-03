'''
Написать функцию print_string_reverse(s)
Функция принимает строку и выводит эту строку в консоль
в обратном порядке.
Если строка равна
None
, пустая или состоит только из
пробелов, функция должна вывести:
Wrong string
'''

def print_string_reverse_1(s):
    if s is None or s.strip() == '':
        print('Wrong string')
    else:
        print(s[::-1])

print_string_reverse_1('    ')

def print_string_reverse_2(s):
    if s is None or s.strip() == '':
        print('Wrong string')
        return
    i = len(s) - 1
    reverse_string = ''
    while i >= 0:
        reverse_string = reverse_string + s[i]
        i = i-1
    print(reverse_string)


print_string_reverse_2('')



'''2.
Написать функцию
is_isr_phone_number(phone)
Функция принимает строку и проверяет, является ли она
израильским номером телефона.
Условия корректного номера:
первая цифра 0;
общее количество символов 10;
все символы являются цифрами.
Если строка соответствует всем условиям, функция
возвращает
True
Если строка не соответствует условиям, функция
возвращает
False
Если строка равна None, пустая или состоит только из пробелов, функция возвращает None
'''

def is_isr_phone_number(s):
    if not s.isdigit():
        return False
    if len(s) != 10:
        return False
    if not s[0] == '0':
        return False

    return True

print(is_isr_phone_number('0534825077'))
print(is_isr_phone_number('3534825077'))
print(is_isr_phone_number('0534a25077'))
print(is_isr_phone_number('05348253077'))
print(is_isr_phone_number('053482507'))

'''
3.
Написать функцию
print_substring_reverse(s, start,
finish)
Функция принимает строку, стартовый индекс и финишный индекс.
Нужно вывести в консоль строку, в которой символы от индекса
start
до индекса
finish
включительно напечатаны в обратном порядке, а остальные символы остаются в обычном порядке
'''

def print_substring_reverse_1(s:str, start:int, finish:int):
    if start > finish:
        return print('wrong args')
    if s is None or s.strip() == '':
        return print('wrong args')
    if start > len(s) or finish > len(s):
        return print('wrong args')
    if start < 0 or finish < 0:
        return print('wrong args')
    return print(s.replace(s[start:finish+1], s[start:finish+1][::-1]))

print_substring_reverse_1('0123456789',3,6)

def print_substring_reverse_2(s, start, finish):
    reversed_sub_string=''
    new_string = ''
    k = finish
    if start > finish:
        return print('wrong args')
    if s is None or s.strip() == '':
        return print('wrong args')
    if start >= len(s) or finish >= len(s):
        return print('wrong args')
    if start < 0 or finish < 0:
        return print('wrong args')

    while k > start:
        reversed_sub_string = reversed_sub_string + s[k]
        k = k - 1
    for i in range(len(s)):
        if i  < start:
            new_string = new_string + s[i]
            i+=1
        else:
            finish = finish + 1
            new_string = new_string + reversed_sub_string
            while finish  < len(s):
                new_string = new_string + s[finish]
                finish+=1
            return print(new_string)

print_substring_reverse_2('0123456789', 3, 6)



def get_words_reverse_1(s):
    one_word_list = s.split()
    res_s = ''
    for i in range(len(one_word_list) - 1, -1, -1):
        res_s += one_word_list[i] + ' '
    return print(res_s.strip())                 #to delete ' space ' after last loop for

get_words_reverse_1('Hellow my nice world')


def get_words_reverse_2(s):
    word = s.split()
    return print(' '.join(word[::-1]))

get_words_reverse_2("Hellow my nice world")

def print_words_reverse_in_column_1(s):
    one_word_list = s.split()
    result_s = ''
    for i in range(0, len(one_word_list), 1):
        result_s += f'{one_word_list[i][::-1]} \n'
    return print(result_s)

print_words_reverse_in_column_1('Hellow my nice world')


def print_words_reverse_in_column_2(s):
    one_word_list = s.split()
    for word in one_word_list:
        print(word[::-1])

print_words_reverse_in_column_2('Hellow my nice world')

