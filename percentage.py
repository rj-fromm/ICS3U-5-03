#!/usr/bin/env python3

# Created by: RJ Fromm
# Created on: november 2019
# This program uses return values


def calculate_area(grade):
    # checks grade
    if grade == "4+":
        mark = "97%"
    elif grade == "4":
        mark = "90%"
    elif grade == "4-":
        mark = "83%"
    elif grade == "3+":
        mark = "78%"
    elif grade == "3":
        mark = "74%"
    elif grade == "3-":
        mark = "71%"
    elif grade == "2+":
        mark = "68%"
    elif grade == "2":
        mark = "64%"
    elif grade == "2-":
        mark = "61%"
    elif grade == "1+":
        mark = "58%"
    elif grade == "1":
        mark = "54%"
    elif grade == "1-":
        mark = "51%"
    elif grade == "R":
        mark = "30%"
    else:
        mark = ("undefined")

    return mark


def main():
    # this function gets length and width

    # input
    grade_user = input("Enter your grade: ")
    print("")

    # call functions
    mark = calculate_area(grade_user)

    print("Your mark is {0}".format(mark))


if __name__ == "__main__":
    main()
