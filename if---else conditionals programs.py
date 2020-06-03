#Lesson 7 Homework
print('Lesson 7 Homework')
#1.Write a program that takes two numbers as inputs. Print the bigger number. 
print('Exercise 1')
a=input('Please enter the first number:a=')
b=input('Please enter the second number:b=')
if a > b:
  print('The bigger number is a')
else:
  print('The bigger number is b')
print('Thank you for entering the numbers')
print()

#2.Write a program that takes a number from a user and tells the user if the number is even or odd.
print('Exercise 2')
number=int(input('Please enter a number:'))
even_or_odd= (number)%2
if even_or_odd==0:
  print(f'The entered number {number} is an even number')
else:
  print(f'The entered number {number} is an odd number')
print('Thank you for entering the number')
print()

#3. Write a program that ask a user for their name and surname and checks if they start with the same letter. Write an appropriate message to the user ('your name & surname start / don't start with the same letter').
print('Exercise 3')
name=input('Please enter your first name:')
print(f'Thankyou for entereing your name. You have entered your name as {name}')
surname=input('Please enter your surname:')
print(f'Thankyou for entering your surname. You have entered your surname as {surname}')
if name[0]==surname[0]:
  print('your name & surname start with the same letter')
else:
  print('your name & surname don\'t start with the same letter')
print(f'Thank you {name}')
print()

#4.Check if the sum of the number of the characters in the name and the surname from ex. 3. is divisible by 3 without a residual. Write an appropriate message to the user.
print('Exercise 4')
name_length= len(name)
print(f'The number of characters in name is {name_length}')
surname_length= len(surname)
print(f'The number of characters in surname is {surname_length}')
add= name_length+surname_length
print(f' The sum of number of characters in the name and surname is {add}')
if add%3==0:
  print(f' Dear user {name} the sum of the number of the characters in name and the surname is divisible by 3')
else:
  print(f' Dear user {name} the sum of the number of the characters in name and the surname is not divisible by 3')
print('Have a nice day')
print()

#or
if((len(name)+len(surname))%3==0):
  print(f' Dear user {name} the sum of the number of the characters in name and the surname is divisible by 3')
else:
  print(f' Dear user {name} the sum of the number of the characters in name and the surname is not divisible by 3')
print('Have a nice day')
print()

#5.Check if both the number of letters in the name and surname are even. Write an appropriate message to the user.
print('Exercise 5')
name_even= name_length%2
surname_even=surname_length%2
if name_even and surname_even:
  print(f'Dear user {name} the number of letters in your name and surname are even')
else:
  print(f'Dear user {name} the number of letters in your name and surname are not even')
print('Have a nice day')
print()

#or
print('Exercise 5')
if((len(name))%2)==0:
  print(f'Dear user {name} the number of letters in your name is even')
else:
  print(f'Dear user {name} the number of letters in your name is not even')
if((len(surname))%2)==0:
  print(f'Dear user {name} the number of letters in your surname is even')
else:
  print(f'Dear user {name} the number of letters in your surname is not even')
print('Have a nice day')
print()