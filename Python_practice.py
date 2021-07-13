print("Hello World")


temperature = int(input("What is the temperature outside? "))
if temperature > 80:
    print("Turn on the AC")
else:
    print("Open the windows.")

#What is the score? 
score = int(input("What is your test score?"))

#Determine the grade. 
if score >= 90:
    print('Your grade is an A. ')
else: 
    if score >= 80:
        print('Your grade is a B. ')
        else:
            if score >= 70:
                print('Your grade is a C.')
            else:
                if score >= 60:
                    print('Your grade is a D. ')
                else:
                    print('Your grade is an F. ')
for county in counties: 
    print(county)
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
for num in range(5):
    print(num)
for i in range(len(counties))
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
 Print(county)
 for county in counties_dict.keys():
     print(county)
for voters in counties_dict.values():
    print(voters)