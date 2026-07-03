#join()
from os import name

words = ['Hellow', 'World', 'and', 'Phyton']
result = ' '.join(words)

print(result)

st = 'b'
if 'a' <= st <= 'd':
    print('Yes')

yalla = 'abwgdejz'
print(yalla[::-1])
print(yalla[3:1:-1])
name = 'Alice'
age = 30
res = f'hi, {name}. Is your age {age}?'
print(res)

#find()
s = 'AbrakadabraAbrakadabra'
sr= 'bra'
print(s.find(sr))
print(s.rfind(sr))
print(s.find('add'))
#count()
print(s.count(sr,4,15))
#split()
print(s.split())
#rjust(), ljust()
s='hi'
print(s.rjust(10, '*'))
print(s.ljust(10, '*'))

test = ['login', 'cart', 'api']
for t in test:
    print(t.ljust(15), 'OK')

order = '125'
print(order.rjust(8, '0'))

print(s.isalpha())
print(s.isdigit())
text = 'qa automation with python'
pos = text.index('automation')
print(pos)
text = 'i like java'
print(text.replace('java', 'phyton'))

text = "2026-07-03"
new_text = text.replace('-', '/')
print(new_text)