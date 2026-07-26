from os.path import sep


class Employee:
    def __init__(self,name,position,salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, value):
        self.__salary = value

    def __str__(self):
        return f'{self.__name} works as {self.__position} and earns {self.__salary}'

    def get_info(self):
        return str(self)

emp = Employee("John", "QA", 5000)
print(emp)
print(emp.get_info())

emp1 = Employee('Vova', 'Devops', 15000)
print(emp1)
print(emp1.get_info())


class Product:
    def __init__(self,name,price,quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,value):
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self,value):
        self.__quantity = value


    def buy_amount(self, amount):
        if self.__quantity >= amount:
            self.__quantity -= amount
        else:
            return print('Not enough products')


    def __str__(self):
       return f'{self.__name} | Price {self.__price} | Quantity {self.__quantity}'



product = Product("Phone", 1000, 5)
print(product)
product.buy_amount(2)
print(product)
product.buy_amount(10)
print(product)



class Vehicle:
    def move(self):
        return 'Vehicle is moving'

class Car(Vehicle):
    def move(self):
        return 'Car is moving'

class Bicycle(Vehicle):
    def move(self):
        return 'Bicycle is moving'


class User:
    country = 'Israel'
    def __init__(self,username,age):
        self.__username = username
        self.__age = age

    def __str__(self):
        return f'{self.__username} {self.__age} {self.country}'

user1 = User('Vova', 29)
user2 = User('Dima', 42)
user3 = User('Anastasia', 26)
print(user1,user2,user3, sep='\n')
User.country = "Canada"
print(user1,user2,user3, sep='\n')
