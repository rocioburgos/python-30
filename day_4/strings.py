''' 
1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
3 Declare a variable named company and assign it to an initial value "Coding For All".
4 Print the variable company using print().
5 Print the length of the company string using len() method and print().'''
print('---------------------------------------------1-5')
concatenate_uno = 'Thirty ' + 'Days ' + 'Of ' + 'Python' 
print(concatenate_uno)
concatenate_dos = 'Coding ' + 'For ' + 'All'
print(concatenate_dos)
company = "Coding For All"
print(company)
print(len(company))

print('--------------------------------------------- 6-10')
'''
6 Change all the characters to uppercase letters using upper() method.
7 Change all the characters to lowercase letters using lower() method.
8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
9 Cut(slice) out the first word of Coding For All string.
10 Check if Coding For All string contains a word Coding using the method index, find or other methods.'''

company = company.upper()
print(company)
company = company.lower()
print(company)

print(company.capitalize())
company= company.title()
print(company)
print(company.swapcase())

print(company[0:6])

print(company.find('Coding') is -1 ) 


print('--------------------------------------------- 11-15')
'''
11 Replace the word coding in the string 'Coding For All' to Python.
12 Change Python for Everyone to Python for All using the replace method or other methods.
13 Split the string 'Coding For All' using space as the separator (split()) .
14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
15 What is the character at index 0 in the string Coding For All.'''

company = company.replace('Coding','Python')
print(company)
company = company.replace('Python','All')
print(company)
company = company.replace('All','Coding')
print(company.split(' '))
company_dos = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company_dos.split(','))

print(company[0])

print('--------------------------------------------- 16-20')
'''
16 What is the last index of the string Coding For All.
17 What character is at index 10 in "Coding For All" string.
18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
19 Create an acronym or an abbreviation for the name 'Coding For All'.
20 Use index to determine the position of the first occurrence of C in Coding For All.'''

print(company)
print(len(company)-1)

print(company[10])

pfe = 'Python For Everyone'
cfa = 'Coding For All' 
letra = 'C'
print(pfe.index(letra))