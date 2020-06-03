print('Hello')
print("Hello")
print('a')
print("a")
print(str())
print(str("newstring"))
name="tom"
print(name)
print(type(name))
mychar="a"
print(mychar)
print(type(mychar))
name1=str()
print(name1)
name2=str("newstring")
print(name2)
print(type(name2))
# How to declare string variables
variable_string_1 = 'hello'
print(variable_string_1)
variable_string_2 = "hola"
print(variable_string_2)
variable_string_3 = str("this is another way...")
print(variable_string_3)
# Even if it's one char, it is still considered as string
one_signle_char= "a"
print(one_signle_char)
print(type(one_signle_char))
# You can also create empty strings
empty_string_1=""
empty_string_2=''
empty_string_3=str()
print('\n')
#operations on string
name="Leopold"
print(name)
print(name[0])
print(name[-7])
print(name[-1])
print(name[-3])
print(len(name))
####### Operations on String variables

my_name = "Mehdi"

# M -> my_name[0] or my_name[-5]
print(my_name[-5])

# I want to access last charater without using any index
my_name_length= len(my_name)
print(f'The length of my name is {my_name_length}')

# I can print the last character just by doing:
print(my_name[len(my_name) - 1]) # this is the same as my_name[5]

# Get the length of the variable

my_blabla_variable = "this isabalabavariBLESHWREAI JUTS WIHRE WHATSHJI AM DRUNK"

print(len(my_blabla_variable))
#practice
myname='shiji'
print(myname)
print(myname[0])
print(myname[-5])
print(len(myname))
myname_length= len(myname)
print(f'The length of my name is {myname_length}')
my_newvariable='i am shiji shajahan studying at redi munich'
print(len(my_newvariable))
print('\n')
#operations on string
#concatenate
s="tom and"+"jerry"
print(s)
#repeatition
s1="this will be reapeated"*3
print(s1)
s2='zZ'
print(s2*10)
# Concatenation (concatenate) -> adding 
string_1="Hello"
string_2="World!"
concatenated_string=string_1 + string_2
print(concatenated_string)
# String multiplication
print(string_1*5)
# Do both
print('zZzZ'*10+'....')
print('\n')
#escape characters
print('This is a backslash \\')
print('I\'m 30 years of old')
print('He said \"Run\"')
print("first line \nSecond Line")
print("\t ... to the right")
# I want to print "Helloooo\"

print("Helloooo\\")

# print I'm happy to meet you

print('I\'m happy to meet you')

# the same rule applies for double quotes

print("I'm \"happy\" to meet you")

# If you use double qoutes, a single quote in the string can be added without backslash
print("I'm what I'm")

# cutting the string into a new line
print("Hello everyone\n I am nice to meet you")

# add horizental table
print("Hello\tSteven")

days= "Mon Tue Wed Thur Fri Sat Sun"
print("Here are the days:", days)
months="Jan\nFeb\nMar\nApr\nMay\nJun\nJul"
print("here are the months:", months)
#input
name=input('What is your name?')
print(f'Hello,{name}!')
#Example1
age=input("How old are you?")
height=input("How tall are you?")
weight=input("How much do you weight?")
print(f"So, you\'re {age} old, {height}tall and {weight}heavy")
######## Let the user enter the input and save it into a variable

#my_input_name = input("Please enter your name: ")
#print(f'you just entered the name {my_input_name}')

#user_age = input("Please enter your age:")
#print(f'the user age is {user_age}')
#print(type(user_age))

# I convert this into an int
#print(type(int(user_age)))

my_input_name1=input("Please enter your name:")
print(f'you just entered your name {my_input_name1}')
user_age=input("please enter your age:")
print(f'the user age is{user_age}')
print(type(int(user_age)))
print(type(user_age))

# Do a addition operation of the user input
first_number= input("Please enter the first number:")#5
second_number=input("Please enter the second number:")#6

# Since the above variables are by default considered as strings
# the below result will simply concatenate the strings
sum_value = first_number + second_number
print(f'the sum of these two numbers is: {sum_value}')

# to do actual numerci operation (we rely on user to enter a numeric user)
sum_value_numeric = int(first_number) + int(second_number)
print(f'the numeric sum of these two numbers is: {sum_value_numeric}')

print('Hi there. I\'m your new bot friend')
name = input('What\'s your name?')
print(f'It\'s really nice to meet you, {name}')
age = input('How old are you, ' + name + '?')
age_in_2_years = int(age) + 2
print(f'Awesome! In 2 years you\'ll be {age_in_2_years} years old')


