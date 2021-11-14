# A program that provides the user with a math quiz
# Date: 10/24/21
# Author: Kevin Owidi

# menu
def menu():
    print("Math quiz")
    print("------------")
    print("1, Addition")
    print("2, Subtraction")
    print("3, Mulitpication")
    print("4, Modulus Division")
    operation = int(input("Select a math quiz operation for a quiz: (1-4): "))
    return operation


# display math functions
def display_math_operation(operation):
    import random
    number1 = random.randrange(3, 20)
    number2 = random.randrange(3, 20)
    # test foe each math operation
    if operation == 1:
        print(" ", number1)
        print("+", number2)
        print("------")
        answer = number1 + number2
    elif operation == 2:
        print(" ", number1)
        print("-", number2)
        print("------")
        answer = number1 - number2
    elif operation == 3:
        print(" ", number1)
        print("*", number2)
        print("------")
        answer = number1 * number2
    elif operation == 4:
        print(" ", number1, "%", number2)
        answer = number1 % number2
    return answer


# check the user's response and compare to the correct answers
def check_user_response(answer):
    response = int(input("Please enter your answer: "))
    if response == answer:
        print("Correct! Great job!")
    else:
        print("Sorry, that is not correct. The correct answer is:", answer)
# mrain program
operation = menu()
answer = display_math_operation(operation)
check_user_response(answer)
