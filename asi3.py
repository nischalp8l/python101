import random

def findOTP(num1,num2):
    x =random.randint(1,20)
    print(x)
    for i in range(3):
        n = int(input("Enter number in range 1 to 20 "))
        if (n>20):
            print("Wrong input try again!")
        elif x==n:
            return "OTP SUCCESSFULLY MATCHED"
        else:
            print("ERROR!!! ENTER THE OTP AGAIN")
    return "SORRY PROGRAM CRASHED"


if __name__ == "__main__":
    num1 = input("Enter your first name ")
    num2 = input("Enter your Last name ")
    print(findOTP(num1,num2))


