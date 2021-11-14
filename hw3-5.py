# A program that provides shipping and total cost
# Date: 10/24/21
# Author: Kevin Owidi

# display the title
print("Shipping Cost calculator")
print()
# create the while loop
while True:
    # get cost from the user
    cost_of_items= float(input("Enter the cost of items ordered: "))
    # validate the user input
    if cost_of_items <0:
        print ("You must enter a positive number. try again: ")
        continue
    # calculate the shipping cost
    if cost_of_items > 75:
        shipping_cost = 0
    elif cost_of_items >= 50:
        shipping_cost = 9.95
    elif cost_of_items >= 30:
        shipping_cost = 7.95
    else: shipping_cost = 5.95
    # calculate the total cost
    total_cost = round(cost_of_items + shipping_cost, 2)
    #display the numbers
    print("Shipping cost:", shipping_cost)
    print("Total cost: ", total_cost)
    # ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != "y":
        break

print("Bye!!!!!!!")