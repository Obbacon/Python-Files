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





