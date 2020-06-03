#Lesson 4 Homework
your_name= input("Please enter your name:")
year_of_birth=input("PLease enter the year you were born:")
salary=input("Please enter your salary:")
rent=input("Please enter how much you pay for rent:")
electricity= input("Please enter how much you pay for electricity bill:")
internet= input("Please enter how much you pay for Internet bill:")
water=input("Please enter how much you pay for water bill:")
food= input("Please enter how much you pay for food and groceries purchase:")
fees= input("Please enter how much you pay for son's school fees:")

basic_needs= int(electricity)+int(internet)+int(water)+int(food)+int(fees)
print(f'Total amount spending out per month for basic needs:{basic_needs}')

balance_amount= int(salary)-int(basic_needs)-int(rent)
print(f'Balance amount avilable per month:{balance_amount}')
percentage_of_saving= input("Please enter how much percent of your remaining salary you want to save:")
saving_per_month= int(balance_amount)*(int(percentage_of_saving)/100)
print(f'Total amount towards saving per month:{saving_per_month}')

months_in_year= input('Please enter the number of months in a year:')
saving_per_year=float(saving_per_month)*int(months_in_year)
print(f'Total amount towards saving per year:{saving_per_year}')

current_age= 2020 - int(year_of_birth)
print(f'Your current age is :{current_age}')
retirement_age= input("Please enter the age of retirement in your country:")
print(f' Your retirement age is: {retirement_age}')
years_to_retirement= int(retirement_age)-int(current_age)

total_rent_until_retirement= int(rent)*int(months_in_year)*int(years_to_retirement)

total_amount_basicneeds= int(basic_needs)*int(months_in_year)*int(years_to_retirement)

total_savings_until_retirement= int(saving_per_year)*int(years_to_retirement)
print(f'Total amount towards saving until retirement is: {total_savings_until_retirement}')

print(f'\"Thank you {your_name} for your input! \n Based on the data you provided, by the age of {retirement_age} your saving will be {total_savings_until_retirement} euros. \n You have {years_to_retirement} years ahead to work. During these days you will be paying:\n\t-{total_rent_until_retirement} euro for rent in total \n\t- {total_amount_basicneeds} euro for basic need in total \n I hope you\'re satisfied with your savings:)\"')


