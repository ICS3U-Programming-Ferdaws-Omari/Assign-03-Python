#!/usr/bin/env python3
# Created by: Ferdaws
# Created in: April, 2022
# This program asks the user for
# the total and let them know
# if they get discount or not
import math
import constants


def main():
    # Let the user know what we are calculating
    print("Today we will calculate the total amount of discount")
    print("you can get in our store ")
    # Get the user total

    try:
        subtotal = float(input("Please enter the amount of your total before tax: "))
        units = input("Enter the currency: ")
        discount = subtotal*0.1
        newsubtotal = subtotal-discount
        tax = newsubtotal * constants.TAX / 100
        total = newsubtotal+tax
    # check the total is equal or more than 1000$
        if subtotal >= constants.TOTAL_DISCOUNT:
            print("you get discount ")
            print("Discount =  {:.2f} {}". format(discount, units))
            print("Tax =  {:.2f} {}". format(tax, units))
            print("Total =  {:.2f} {}". format(total, units))
    # check the numbers is less than 1000$
        else:
            print("you don't get discount")
            print("You need 1000$ to get a discount")
    except Exception:
        print("This was not an integer, please enter an integer")
    finally:
        print("Thanks for coming")


if __name__ == "__main__":
    main()
