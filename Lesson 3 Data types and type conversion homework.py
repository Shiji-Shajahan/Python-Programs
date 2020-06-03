#Homework 3
#Exercise1
"""1. Save the following information in variables (with meaningful names) and explain what data type they would be and why (you could explain this on a comment):
Your name
Your age
The price of a breze 
"""

print('Exercise1')
#Your name
my_name = 'Shiji Shajahan'
print(f'My name is {my_name}')
print(my_name)
print(type(my_name))
# value of variable My_name is of datatype string since its a sequence of characters in single quotes
#Your age
my_age = 30
print(f'I am {my_age} years of old')
print(my_age)
print(type(my_age))
#value of variable My_age is of datatype Integer since value 30 is whole number without decimal point
#The price of a breze
breze_price = 1.29
print(f'The price of a breze is {breze_price}')
print(breze_price)
print(type(breze_price))
# value of variable breze_price is of datatype float since the value 1.29 is a number with decimal point
print()

#Exercise2
"""
2. Correct these lines of code using type conversion. Then print the result and its data type.
price_3_books = '5.0' * 3
my_age = 'I am ' + 26
total_bill = 4.45 + 3.30 + 6 + '7'
"""

print('Exercise2')
#Type conversion
#price_3_books = '5.0' * 3
#method1
#'5.0' is now a string, so need to change the value to number by removing the quotes for multiplication operation. 5.0 is a float datatype due to the presence of decimal point
price_3_books = 5.0 * 3
print(f'The price of 3 books is {price_3_books}')
print(price_3_books)
print(type(price_3_books))
print()

#method2
price_1_book = float('5.0')
print(price_1_book)
print(type(price_1_book))
price_3_book = price_1_book*3
print(f'The price of 3 books is {price_3_book}')
print(price_3_book)
print(type(price_3_book))
print()

#my_age = 'I am ' + 26
#' I am' is a string but + 26 is integer, so entire characters are included in string
my_age = 'I am ' + str(26)
print(my_age)
print(f'{my_age} years of old')
print(type(my_age))
print()

#total_bill = 4.45 + 3.30 + 6 + '7'
billvalue_4= float('7')
print(billvalue_4)
total_bill = 4.45 + 3.30 + 6 + billvalue_4
print(f'The total bill is {total_bill}')
print(total_bill)
print(type(total_bill))

#Exercise3
#3. Convert 2020 to all the data types we learnt and print the type for all of them.

print('Exercise3')
#Stringdatatype
year_1= str(2020)
print(year_1)
print(type(year_1))
#Integerdatatype
year_2= int(2020)
print(year_2)
print(type(year_2))
#floatdatatype
year_3= float(2020)
print(year_3)
print(type(year_3))
