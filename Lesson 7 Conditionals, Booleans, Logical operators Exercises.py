print('Lesson 7 Exercise 1')
#Birthday video-call bot
print('Birthday video-call bot')
#Ask a user to input their name and greet them in a form ‘Hello, XYZ. Welcome to my online celebration’
name= input('Please Enter user name:')
print(f'Hello, {name}. Welcome to my online celebration')
#Ask the user to input their age and check if the user is at least 18. If yes, invite them to the party.
age= int(input('Please enter your age:'))
no_of_years= 18 - (age)
if age > 18:
  print('Please attend the party')
else:
  print(f'Please do attend the meeting at age of 18 in {no_of_years} years')
print('Take care')
print()

print('Exercise 3 - check it with python')
a= input('Please enter a value:')
b= input('Please enter a value:')
print((not a and not b) == (not (a and b)))
print((not (a or b)) == (not a and not b))
print((not (a and b)) == (not a or not b))
print(a or not a == True)
print(a or not a)





