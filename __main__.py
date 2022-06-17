# pizza with pineapple or not
def main():
    print("This program will calculate the cost of a pizza")
    diameter = int(input("Enter the diameter of the pizza: "))
    if diameter > 12:
        print("Sorry, we can't make a pizza that big")
    else:
        cost = calculate_cost(diameter)
        print("The cost of the pizza is: $" + str(cost))
