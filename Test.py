# A program for telling the user in what year they will turn 100

import datetime


def test():
    name = input("Please enter your name: ")
    print("Your name is " + name)

    age = int(input("Please enter your age: "))

    age_later = (100 - age)

    age_later = str(age_later)

    abc = datetime.datetime.now()

    now_year = abc.year

    turn_100 = (100 - age) + now_year

    print(name + " will turn 100 years old after " + age_later + " year(s)" + " in the year " + str(turn_100))

test()

'''
print("Were " + "wolf")
print("Door " + "man")
print("4" + "chan")
print(str(4) + "chan")
print(4 * "test")
'''

# Prints out numbers which are divisible by 7 but are not a multiple of 5 between the numbers 2000 and 3201                                     5

"""
stuff = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        stuff.append(str(i))


print(','.join(stuff))
"""



