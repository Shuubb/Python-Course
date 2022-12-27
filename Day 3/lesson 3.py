import random

#My_Name = "Davit Shubitidze"

# if " " in My_Name:
#     print(My_Name)


# My_Firstname = "Davit"
# My_Surname = "Shubitidze"
# My_age = 19
# My_Profession = "Programmer"
# My_Sentance = "\nName: {} {}. \nAge: {}. \nProfesion: {}.\n".format(My_Firstname, My_Surname, My_age, My_Profession)

# print(My_Sentance)

# My_Name = "Davit Shubitidze"
# Number = random.random()

# print(Number)

# if Number > 0.5:
#     My_Name = My_Name.replace(' ', '#')

# if '#' in My_Name:
#     print("\nThere is Reshotka in my name yay!\n")
# else:
#     print("\nThere is no Reshotka in my name :(\n")

# My_Name    = input("\n   Enter Your Name: ")
# My_Surname = input("Enter Your Surname: ")
# while True:
#     try:
#         My_Age = int(input("    Enter Your Age: "))
#     except ValueError:
#         print("Please enter number!")
#         continue
#     break

# My_Sentence = "\nHello! So your name is {} {} and you are {}, Nice to meet you!".format(My_Name, My_Surname, My_Age)
# print(My_Sentence)

# while True:
#     try:
#         Years_Gone = int(input("Enter Your's Gone: "))
#     except ValueError:
#         print("Please enter number!")
#         continue
#     break

# My_Age += Years_Gone
# My_Sentence = "\nSo! {} Years has gone and now you are {}!\n".format(Years_Gone, My_Age)
# print(My_Sentence)
while True:
    try:
        Number_1 = int(input("\n Insert First Number: "))
    except ValueError:
        print("\nInsert Number Please!")
        continue
    break
while True:
    try:
        Number_2 = int(input("\nInsert Second Number: "))
    except ValueError:
        print("\nInsert Number Please!")
        continue
    break

Result = Number_1*Number_2

if Result > 100:
    print('\n', Result)
else:
    print("\nYou Lost!")


print('\n')