#Lesson 6 - Sets & Dictionaries
str1="word1 word2 word3"
print(str1.split(" "))
numbers = [2, 3, 1]
groceries = ["milk","bread","cheese"]
print(max(numbers))
print(min(numbers))
print(max(groceries))
print(min(groceries))
#print(max('foobar',10))
list1=[2,3,'sky']
list1.append(3)
print(list1)
list1.remove(3)
print(list1)

list1.remove(3)
print(list1)
#Sets
#Define a set
set1= {1,2,3}
print(set1)
print(type(set1))
set2={1,2,3,2,2}
print(set2)
print(type(set2))
#how to print length of a set
print('length')
print(len(set1))
print(len(set2))
#print(set2[1])
#set with different datatypes
set3={3,"dog",4.5}
print(set3)
print(type(set3))
print("hallo" in set3)
print("dog" in set3)
#set operations
set4={1,3,4,"a"}
set5={1,3}
#intersection
print('Intersection')
print(set4.intersection(set5))
#Union
print('union')
print(set4.union(set5))
#difference
print('difference')
print(set4.difference(set5))
#check the subset
print('subset')
print(set4.issubset(set5))
print(set5.issubset(set4))
print(set4.issubset(set4))

print('\n')
print('dictionaries')
my_dictionary={'hello':'hallo','one':'eins','apple':'Apfel'}
print(my_dictionary)
#another way
#my_dictionary1={
              #'hello':'hallo',
              #'one':'eins',
              #'apple':'Apfel'
              #}
 #print(my_dictionary1)
#length
print('length')
print(len(my_dictionary))
print(type(my_dictionary))
print(my_dictionary["hello"])
print(my_dictionary["one"])
#add new key and Value
print('Add new key and value')
my_dictionary["sun"]="sonne"
print(my_dictionary)
#my-dictionary["say"]=["sagen","tell"]
#print(my_dictionary)
#different datatypes
print('differentdatatypes')
dict2={
  1:"hello",
  2:[6,7,8],
  3:7.8
}
print(dict2)


