'''
Exercises: Level 1
1 Declare an empty list
2 Declare a list with more than 5 items
3 Find the length of your list
4 Get the first item, the middle item and the last item of the list
5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
'''
print('---------------------------------------------1-5')
mi_lista = list()
print(mi_lista)

cantantes = ['Bad Bunny', 'ROSALIA', 'Julieta Venegas', 'Cazzu', 'Dua Lipa', 'Lana Del Rey', 'QUEEN', 'Alvaro Diaz' ]
print(len(cantantes))
print('Primer cantante: ' ,cantantes[0])
index_medio= (len(cantantes)-1)//2
index_last= len(cantantes)-1 
print('Cantante del medio: ', cantantes[index_medio])
print('Cantante final: ', cantantes[index_last])



mixed_data_types = ['Rocio', 21321321, 180, 'S', 'Calle falsa 1234']
print(mixed_data_types)

''' 
6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
7 Print the list using print()
8 Print the number of companies in the list
9 Print the first, middle and last company
10 Print the list after modifying one of the companies
'''
print('---------------------------------------------6-10')
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


print('---------------------------------------------11-15')
'''
11. Add an IT company to it_companies
12. Insert an IT company in the middle of the companies list
13. Change one of the it_companies names to uppercase (IBM excluded!)
14. Join the it_companies with a string '#;&nbsp; '
15. Check if a certain company exists in the it_companies list.
'''
it_companies.append('Mercado Libre')
it_companies.insert( 4, 'Intel')
it_companies[0] = it_companies[0].upper()
print(it_companies)

dato = '#;&nbsp; '
result = dato.join(it_companies)
print(result)

print('¿Existe IBM en la lista? ' , 'IBM' in it_companies)


print('---------------------------------------------16-20')
'''
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
'''
print('Lista antes de ordenar: \n', it_companies)
it_companies.sort()
print('Lista ordenada: \n',it_companies)

it_companies.reverse()
print('Reverse: ',it_companies)

print('Slice out the first 3 companies : ', it_companies[0:3])
print('Slice out the last 3 companies : ', it_companies[-3:])
print('Slice out the middle company : ', it_companies[ ((len(it_companies)-1)//2)  ])


print('---------------------------------------------21-25')
'''
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies from the list
25. Destroy the IT companies list
26. Join the following lists:
    ```py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    ```
27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. 
Then insert Python and SQL after Redux.
'''
print('Lista antes de eliminar elementos: \n', it_companies)


it_companies.pop(0)
print('Remove the first IT company from the list ', it_companies)
it_companies.pop((len(it_companies)-1)//2)
print('Remove the middle IT company or companies from the list: ' ,it_companies)
it_companies.pop(-1)
print('Remove the last IT company from the list: ',it_companies)
it_companies.clear()
print('Remove all IT companies from the list: ', it_companies)
print('Destroy the IT companies list ')
del it_companies 


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB'] 
joineada = front_end + back_end
full_stack = joineada.copy()
print(full_stack)


 