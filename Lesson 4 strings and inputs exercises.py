#Exercise 1 – String Operation
#Write a program that prints a shopping list as following:

print("shopping list:\n\t*bread\n\t*milk\n\t*coffee\n\t*bananas")
print()

#Exercise 2 – Input
"""
1) Ask the user of your program to enter following information:
- Name
- Month of birth 
- Year of birth

Once the information is provided, print following message:
"Hello {user_name}, by the next {birth_month} you will be {user_age} years old!"

2) Write a small program (2 lines of code :)) that asks the user to enter a text and prints the length of the input text.
"""

user_name= input('please enter your name:')
birth_month= input('please enter your month of birth:')
year_of_birth= input('please enter your year of birth:')
user_age= (int(2020) - int(year_of_birth))
print(user_age)
print(f'Hello {user_name},by the next {birth_month}, you will be {user_age} years old!')

your_name= input('please enter your official name')
print(len(your_name))