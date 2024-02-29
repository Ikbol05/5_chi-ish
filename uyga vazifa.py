
# 1 chi masala

# Figure = type("Figure", (), {"get_name": lambda self: self.name})
#
# Triangle = type("Triangle", (Figure()), {"A": "a", "B": "b", "C": "c"})
#
# Square = type("Square", (Figure()), {"A": "a", "B": "b", "C": "c", "D": "d"})
#
# Cirkle = type("Cirkle", (Figure()), {"R": "r"})

#===============================================================================================================

# 2 chi masala

# class Car(type):
#
#     def __new__(cls, model, color, speed, attrs):
#         attrs["model"] = "Captiva"
#         attrs["color"] = "Qora"
#         attrs["speed"] = 220
#         return type(model, color, speed, attrs)
#
# class User(metaclass=Car):
#     pass
#
#
# user = Car()
# print(user.model)
# print(user.color)
# print(user.speed)

#===============================================================================================================


# 3 chi masala\


# class Table(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['id'] = 0
#         attrs['name'] = ''
#         attrs['phone'] = ''
#         attrs['address'] = ''
#         return ( name, bases, attrs)
#
# class Table(metaclass=Table):
#     pass
#
#
# n1 = Table()
# n1.id = 1234
# n1.name = "Iphone"
# n1.phone = "12"
# n1.address = "Russia"
#
# print(f"ID: {n1.id}, Name: {n1.name}, Phone: {n1.phone}, Address: {n1.address}")




































































































