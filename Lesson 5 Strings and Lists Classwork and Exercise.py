name="Eva"
secondname="Ramaj"
#print E
print(name[0])
print(name[-3])
#print a
print(name[2])
print(name[-1])
#print EvaRamaj
print(name+secondname)
#print Eva Ramaj
print(name+ " " +secondname)
#print eva on first line and ramaj on second line
print(name+ '\n'+secondname)
print(len(name))
print(len(secondname))
print(name*3)
print(len(name*3))
#Find
a = "Hello World"
print(a.find("e"))
print(a.find("o"))
print(a.find("a"))
#count
b="blablabla"
print(b.count("a"))
print(b.count("b"))
#replace
my_str="ReDi is Awesome"
print(my_str.replace("is", "always will be"))
my_str1="ReDi is Awesome"
new_string=my_str1.replace("is","always will be")
print(new_string)
print()


#exercise1
"""1. You have a following string: my_str = 'thequickbrownfoxjumpsoverthelazydog'
Write a Python program which asks the user about a character which he or she wants to count on the string my_str.
Expected output :
"Which character do you want me to count?" -> "o"
The character "o" has appeared 4 times.
"""
print('String Exercise 1')
my_str= 'thequickbrownfoxjumpsoverthelazydog'
print(my_str)
character1=input("\"Which character do you want me to count?\"")
how_many_c1= my_str.count(character1)
print(f'The character \"{character1}\" has appeared {how_many_c1} times')
character2=input("\"Which character do you want me to count?\"")
how_many_c2= my_str.count(character2)
print(f'The character \"{character2}\" has appeared {how_many_c2} times')
print('\n')
print('\n')


#list
#empty list
my_list1=[]
#list with numbers or intergers
my_list2=[1,2,3]
#list with mixed datatypes
my_list3=[1,"bread",3.4]
list_shopping=["bread","sausages","banana","milk"]
#print bread
print(list_shopping[0])
numbers=[1,2,3,4,5]
#print4
print(numbers[3])
print(numbers[-2])
#print2
print(numbers[1])
print(numbers[-4])

#mutable
numbers[1]=10
print(numbers)
list_shopping[2]="chocolate"
print(list_shopping)
#length of list
print(len(list_shopping))
print(len(numbers))
#find the sum of the list
numbers1=[1,2,3,4,5]
print(sum(numbers1))
#append an element
numbers1.append(100)
print(numbers1)
numbers1.remove(1)
print(numbers1)
numbers2=[2,32,4,56,78]
numbers2.remove(32)
print(numbers2)
list_shopping.remove("bread")
print(list_shopping)
#sorting the list
list_shopping.sort()
print(list_shopping)
numbers2.sort()
print(numbers2)
alphabets=['b','g','f','a']
alphabets.sort()
print(alphabets)
my_list=[0,10,3,14]
print(len(my_list))
print(sum(my_list))
my_list.append(30)
print(my_list)
my_list.remove(0)
print(my_list)
my_list.sort()
print(my_list)
print('\n')
print('\n')

#exercise1 list
#my_list = [0, 20, 30, 42, 2, 5]
#Print your list “my_list”
#Print the length of the list
#Print the sum of all elements
#Print the smallest and biggest element of your list 
#Add element 34 on the list

my_list1=[0,20,30,42,2,5]
print(my_list1)
print(len(my_list1))
print(sum(my_list1))
my_list1.sort()
print(my_list1)
print(my_list1[0],my_list1[-1])
my_list1.append(34)
print(my_list1)
print(max(my_list1))
print(min(my_list1))
