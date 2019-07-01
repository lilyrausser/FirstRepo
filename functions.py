def factorial (n): 
    """Returns the factorial of n"""

    if n == 1: 
        return 1
    else: 
        return n * factorial(n-1)
input_number = input("pick a number: ")

result = factorial(int(input_number))

print("The factorial of " + input_number + " is: " + str(result))

