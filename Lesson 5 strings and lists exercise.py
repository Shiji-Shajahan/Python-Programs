#strings Exercise2
#2.Given 2 strings, s1 ="Petao" and s2="Yshan", return a new string made of the first, middle and last char of each input string
#Expected output:
#Python

print('strings_Exercise2')
s1="Petao"
s2="Yshan"
print(f'Length of string 1 is: {len(s1)}')
print(f'Length of string 2 is: {len(s2)}')
s1_first= s1[0]
print(s1_first)
s2_first= s2[0].lower()
print(s2_first)
s1_middle=s1[2]
print(s1_middle)
s2_middle=s2[2]
print(s2_middle)
s1_last=s1[-1]
print(s1_last)
s2_last=s2[-1]
print(s2_last)
print(s1_first+s2_first.lower()+s1_middle+s2_middle+s1_last+s2_last)
print(s1[0]+s2[0].lower()+s1[2]+s2[2]+s1[-1]+s2[-1])
print('\n)')
print('\n)')


#List Exercise2
#Create a shopping list with 3 elements
#Define and print the shopping_list
print('List Exercise2')
shopping_list=[]
print(shopping_list)
#A list named shopping list is created , initially its an empty list and it is printed
#Add three more elements to the shopping list, by using input() and shopping_list.append()
shopping_list.append(input('what would you want to add:'))
shopping_list.append(input('what would you want to add:'))
shopping_list.append(input('what would you want to add:'))
print(shopping_list)
#Sort the shopping list alphabetically
shopping_list.sort()
print(shopping_list)
#Remove the second element from your list
shopping_list.remove(shopping_list[1])
print(shopping_list)


