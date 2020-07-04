def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    # It's based on a simple math trick.
    # for each number ranging from 0 to 104 the calculation will result in the number itself.
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7. One imput at a time')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start learning to program if you haven't started "
                                      "already!")


def count():
    print('Now I will prove to you that I can count to any number you want. Please enter any number you want me to '
          'count to.')

    num = int(input())
    print("Here we go...")
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Alright. Let's test your programming knowledge.")
    print("""
    Why do we use methods? Enter the number correspondinng to your answer.
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.
    """)
    response = int(input())
    while response != 2:
        print("Please, try again.")
        response = int(input())
    print("That's CORRECT!!!")


def end():
    print('Thank you for taking time to have a short chat with Chatty Phil. Have a nice day! :)')


# Testing script...
greet('Chatty Phil', '2020')
remind_name()
guess_age()
count()
test()
end()
