
#Python program to take a number from the user, check if its even or odd, check if its positive or negative, find its square and its cube and then print

def evenorodd(num):
    """evenorodd function finds out if the input is odd or even"""
    if num%2==0:
        print("Number is even")
    else:
        print("Number is odd")



def posorneg(num):
    """function posorneg is to find out if its positive or negative"""
    if num >= 0:
        print("Number is postive")
    else:
        print("Number is negative")

def squareandcube(num):
    """The next function squareandcube is to find the square and cube of the input"""""
    square=num**2
    cube=num**3
    print("Square is: ", square)
    print("Cube is, ", cube)
def main():
    """This calls the main function and then we call the functions within main and use number input in the placeholder of num in the 4 other functions."""""
    number= int(input("Enter a Number: "))
    evenorodd(number)
    posorneg(number)
    squareandcube(number)
main()
