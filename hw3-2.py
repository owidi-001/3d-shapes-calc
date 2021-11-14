# A program that calculates HFC tuition based on location and number of credits
# Date: 10/24/21
# Author: Kevin Owidi

# display a welcome or title message
print("HFC Tuition Calculator")
print()
#tuition calculator function
def tuition_calculator (type, credit1, credit2):
    if type == 1:
        tuition = (credit1 * 105.75) + (credit2 * 200)
    elif type == 2:
        tuition = (credit1 * 184.50) + (credit2 * 265)
    elif type == 3:
        tuition = (credit1 * 267.50) + (credit2 * 350)
    return tuition

# menu
print("1 - In District Student")
print("2 - Out of District Student")
print("3 - Out of District and International student")
type = int(input("Choose one of the above (1-3): "))
# get number of credits
credit1 = int(input("How many 100-200 level credits do you plan to register for? "))
credit2 = int(input("How many 300-400 level credits do you plan to register for? "))
# call the tuition function
tuition  = tuition_calculator(type, credit1, credit2)
# display the tuituion
print("Your tuition cost will be $ {:,.2f}".format(tuition))


