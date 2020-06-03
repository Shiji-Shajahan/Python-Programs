#Lesson 6 Homework
print('Lesson 6 Homework')
course_name= "Introduction to Magic"
print(f'The course name offered by ReDI School is {course_name}')
print(f"This is a report about the \'{course_name}\' course.")
print('\n')

# Here, we define a list of students in the class.
students = ['Michael', 'Kate', 'Scott', 'Lauren', 'Christopher']
print(f'The students in our class are: {students}')
print('\n')

# Here, we define a list of grades for a mid-term exam.
grades = [100, 60, 55, 82, 90]
print(f'The grades on the mid-term exam are: {grades}')
print('\n')

# 1. Using the function `max` on the `grades` list, define the variable 
# `best_grade` to be the max grade of the students.
best_grade = max(grades)
print(f'The best grade in the class is: {best_grade}') 

# 2. Using the function `min` on the `grades` list, define the variable 
# `worst_grade` to be the min grade of the students.
worst_grade = min(grades)
print(f'The worst grade in the class is: {worst_grade}') 
print('\n')

# 3. Using the functions `sum` and `len` on the `grades` list as well as basic
# math operations, define the variable `avg_grade` as the average grade of the students.
student_strength= len(students)
print(f'student_strength in the class is:{student_strength}')
avg_grade = sum(grades)/student_strength
print(f'The average grade in the class is: {avg_grade}') 
print('\n')

# 4. Let's assume 'Alice' just joined the class. Add a line of code below,
# which modifies the `students` list using the `append` operation in order to
# add 'Alice' to the list of students.
students.append('Alice')
print(f'A new student, Alice, just joined the class!')
print(f'The students in our class are now: {students}')
print('\n')

# Let's try a different data structure for storing the final exam grades. We'll
# use a dictionary.
final_grades = {
    'Michael': 89,
    'Kate': 100,
    'Scott': 75,
    'Lauren': 90,
    'Christopher': 60,
    'Alice': 84
}

# 5. Fix the print statement to print Michael's final exam grade by using the
# 'Michael' key to look up his grade in the `final_grades` dictionary
print(f"Michael's final exam grade is {final_grades['Michael']}")

# 6. Print the other students' final exam grades the same way you printed
# Michael's.
print(f"Kate's final exam grade is {final_grades['Kate']}")
print(f"Scott's final exam grade is {final_grades['Scott']}")
print(f"Lauren's final exam grade is {final_grades['Lauren']}")
print(f"Christopher's final exam grade is {final_grades['Christopher']}")
print(f"Alice's final exam grade is {final_grades['Alice']}")
print('\n')

# 7. One teacher realizes he made an error with Christopher's final exam
# grade. Christopher actually got a 87. Fix his grade in the `final_grades` dictionary
# by updating the value for the key 'Christopher' (not by recreating a new
# dictionary).
final_grades['Christopher']=87
print(f"Whoopsi, I made a mistake with Christopher's final exam grade. His grade is actually {final_grades['Christopher']}.")
print('\n')

# This `set` function creates a set from the list of students.
all_students = set(students)
passed = {'Michael', 'Lauren', 'Christopher', 'Alice'}
print(f'The students who passed my class are: {passed}')

# 8. Using the `difference` set operation, define variable `failed` as the set of 
# students who did not pass the class.
failed = all_students.difference(passed)
print(f'The students who failed my class are: {failed}')
print('\n')
women = {'Kate', 'Lauren', 'Alice'}

# 9. Using the `intersection` set operation, define `passing_women` as the set of
# women who passed the class.
passing_women = passed.intersection(women)
print(f'The women who passed my class are: {passing_women}')
print('\n')

teachers = {'Harry', 'Emma'}
# 10. Using the `union` set operation, assign `all_people` the set of
# all people, i.e. students and teachers, who are participating in this class.
all_people =all_students.union(teachers) 
print(f'The students and teachers participating in this class are: '
      f'{all_people}')
      

# Optional BONUS: Create a few other report information. Feel free to be 
# creative by creating new sets or writing new statistics!

print('\n')
#Total men students in class
men=all_students.difference(women)
print(f'All men students in my class are:{men}')
#men who passed the class
passing_men= passed.difference(women)
print(f' The men who passed my class are:{passing_men}')
#failed men students in class
failed_men=men.difference(passing_men)
print(f'The men students failed in my class are:{failed_men}')