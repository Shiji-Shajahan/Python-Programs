#Excersice1
#Are these variable names correct? Could they be improved?​
#a = 5.0 correct
#NeWvArIaBle = 'hello' variable name complex and casesensitive
#​my_name='Wolfgang'
#variable name incorrect and its using character otherthan underscore 
#2nd_name = 'Amadeus'
#incorrect since variable name should start with letter
#_my_age = 26 
#correct since variable name can start with underscore
#origincountry = 'Austria'
#correct and variable name is descriptive and readble
print()

print('Advanced operators and Variables')
print('Exercise 2')
a=2**3
print(a)
b=a//2
print(b)
c=25//2
print(c)
d = 23%4
print(d)
a= c%d
print(a)
e=-11//3
print(e)
f=-11/3
print(f)
print()

print('Exercise 2')
print('Type conversion')
"""
What was the original type? Print the result
a = float('25')
b = str(6234)
c = float('0.45')
d = int(24.6)  # What happened in this example?
e = int('hello')  # And in this one?
"""
a=float('25')
print(a)
print(type(a))
#a='25' is a string

b=str(6234)
print(b)
print(type(b))
#b=6234 is an integer

c=float('0.45')
print(c)
print(type(c))
# c='0.45' is a tring

d=int(24.6)
print(d)
print(type(d))
#d=24.6 isfloat

#e=int('hello')
#is not possible, sincee 'hello' is a string and not an integer