'''
Exercises: Level 1
1 Declare an empty list
2 Declare a list with more than 5 items
3 Find the length of your list
4 Get the first item, the middle item and the last item of the list
5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
'''

mi_lista = list()
print(mi_lista)

cantantes = ['Bad Bunny', 'ROSALIA', 'Julieta Venegas', 'Cazzu', 'Dua Lipa', 'Lana Del Rey', 'QUEEN', 'Alvaro Diaz' ]
print(len(cantantes))
print('Primer cantante: ' ,cantantes[0])
index_medio= (len(cantantes)-1)//2
index_last= len(cantantes)-1 
print('Cantante del medio: ', cantantes[index_medio])
print('Cantante final: ', cantantes[index_last])



mixed_data_types = ['Rocio', 26, 165, 'S', 'Calle falsa 1234']
print(mixed_data_types)

''' 
6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
7 Print the list using print()
8 Print the number of companies in the list
9 Print the first, middle and last company
10 Print the list after modifying one of the companies
'''
it_companies = list(['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'])
print(it_companies)
print(' number of companies in the list: ',len(it_companies))
index_first = 0
index_medio = (len(it_companies)-1)//2
index_last = len(it_companies)-1 
print(it_companies[index_first])
print(it_companies[index_medio])
print(it_companies[index_last])

it_companies[3] = 'Appppppple'
print(it_companies)

