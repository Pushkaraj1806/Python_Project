#importing required libraries
import os
import time

#perform addition
def addition():
    nums = list(map(int, input("Enter the required numbers seperated by space: ").split()))
    return sum(nums)

#perform substraction
def subtraction():

    n1 = float(input("Enter First Number: "))
    n2 = float(input("Enter Second Number: "))

    return n1 - n2

#perform multiplication
def multiplication():
    nums = list(map(int, input("Enter the required numbers seperated by space: ").split()))
    res = 1
    for num in nums:
        res *= num
    return res


#perform division
def division():
    n1 = float(input("Enter First Number: "))
    n2 = float(input("Enter Second Number: "))

    return n1 / n2


#calculate average
def average():
    nums = list(map(int, input("Enter the required numbers seperated by space: ").split()))
    return sum(nums) / len(nums)


c = 0
while c != "-1":

    print("Enter '1' for Addition")
    print("Enter '2' for Subtraction")
    print("Enter '3' for Multiplication")
    print("Enter '4' for Division")
    print("Enter '5' for Average")
    print("Enter '-1' to Exit.\n")

    c = input("Enter Your choice here: ")

    if c == "1":
        res = addition()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif c == "2":
        res = subtraction()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif c == "3":
        res = multiplication()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif c == "4":
        res = division()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif c == "5":
        res = average()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif c == "-1":
        os.system("cls")
        print("Thank you for using my Calculator!")
        time.sleep(2)
        break

    else:
        os.system("cls")
        print("Sorry, This is invalid option!")
        time.sleep(2)
        os.system("cls")