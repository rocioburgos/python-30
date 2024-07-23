import math
#Day 2: 30 Days of python programming
#Declarar variables
first_name = 'Rocio'
last_name = 'Burgos'
full_name = 'Rocio Burgos'
country = 'Argentina'
city = 'Buenos Aires'
age = 26
year = 2024
is_married = True 
is_true = True
is_light_on = True 
day , month, week ='Monday', 'July', 23


#Ver el tipo de dato de las variables

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(day))
print(type(month))
print(type(week))
#

print(len(first_name))
print("Last name vs first name : ",len(last_name) , len(first_name))


num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two %  num_one
exp = num_one ** num_two
floor = num_one // num_two


area_of_circle = math.pi * (30 ** 2)
circum_of_circle = 2 * math.pi * 30 

area_user = input("Ingrese el radio de un circulo: ")
print(math.pi * (int(area_user) ** 2))