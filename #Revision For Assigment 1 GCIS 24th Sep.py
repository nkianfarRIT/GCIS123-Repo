#Revision For Assigment 1 GCIS 24th Sep

#Program to check if a number is even or odd, positive or negative, its square and its cube.

def EvenOdd(placeholder):
    """This first function will tell us whether an inputted number is even or odd. We use placeholder as a placeholder till we use a different value in its place."""
    if placeholder % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd")

def PosNeg(placeholder):
    """This second function will tell us whether the inputted number is positive or negative by seeing whether it is greater than zero
    note: It has to be greater than zero and not greater than and equal to zero"""
    if placeholder > 0:
        print("Your number is positive, just like me :-)")
    else:
        print("Your number is negative, just like my personality ;-( )")

def Sqaured(placeholder):
    """This third function will give us the square of our inputted number by using the simple mathemtical operators
    note: There is an alternative way to do this instead of doing **2 we can just do placeholder*placeholder."""
    SquaredNumber = placeholder**2
    print("The square of your number is: " , SquaredNumber)

def Cubed(placeholder):
    """This fourth function will give us the cube of our inputted number using the simple mathematical operators
    note: There is an altrnative way to do this instead of doing **2 we can do placeholder*placeholder*placeholder"""
    CubedNumber = placeholder**3
    print("The cube of your number is: " , CubedNumber)

def main():
    """This fifth and final function is the main function where we input our given number into all our other functions."""
    number = int(input("Please enter any non-zero integer number: "))
    EvenOdd(number)
    PosNeg(number)
    Sqaured(number)
    Cubed(number)
    print("GoodBye!")

#Now we will call the main function:
main()





