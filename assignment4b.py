#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: October 2019
# This program determines whether the employee is able to get the bonus or not

import constants


def main():
    # input
    salary = input("Please enter your yearly salary: $")
    years_of_service = input("Please enter the number of years of service: ")
    print("")
    # process & output
    # try catch
    try:
        integerAsNumber1 = int(salary)
        integerAsNumber2 = int(years_of_service)

        # calculating whether the emplyess are able to get bonus or not
        if integerAsNumber2 >= constants.BONUS_YEAR:
            print("Your new net salary is ${}" .format
                  (round(integerAsNumber1*1.05)))
        else:
            print("Sorry, you aren't able to get 5% due to years of service")
    except Exception:
        print("Invalid entry. Please try again")
    finally:
        print("Thanks for using my program")


if __name__ == "__main__":
    main()
