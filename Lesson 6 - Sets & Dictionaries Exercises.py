#Exercise 2 (dictionaries)
print('Exercise 2 (dictionaries)')
luggage = {'bag' : ['smartphone', 'chewing gums', 'wallet'],
           'backpack' : ['laptop', 'notepad', 'sandwich', 'energy drink']}
#Add a key to luggage called ‘pocket' and set its value to be the integer 50.
print('Add a new key and value')
luggage["pocket"]=50
print(luggage)
print('\n')

#.sort() the items in the list stored under the 'backpack' key.
print('Sort items in list')
luggage['backpack'].sort()
print(luggage)
print('\n')

#Then .remove('sandwich') from the list of items stored under the 'backpack' key
print('Remove one value from the list')
luggage['backpack'].remove('sandwich')
print(luggage)
print('\n')

#Add 10 to the number stored under the key 'pocket'.
print('Add value 10 to the key "pocket"')
luggage['pocket']+=10
print(luggage)
print('\n')


#Exercise1
print('Excercise1')
all_people = {'adrian', 'edward', 'emily', 'laura', 'kevin', 'bella'}
vampires = {'edward', 'laura'}
women = {'emily', 'laura', 'bella'}
zombies = {'emily'}
#Print the set of all women that are vampires. 
print('set of all women that are vampires')
print(women.intersection(vampires))
#Define a new set “men” that contains all men, i.e., all persons that are not women. 
print('set of all men that are not women')
men= all_people.difference(women)
print(men)
#Print the set of all men that are not vampires. 
print('set of all men that are not vampires')
print(men.difference(vampires))
#Print the set of all persons that are either vampires or zombies.
print('set of all persons that are either vampires or zombies')
print(vampires.union(zombies))






