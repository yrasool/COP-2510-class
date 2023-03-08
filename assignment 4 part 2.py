#U67661285
#Yusra Rasool
#IN the below code the function operate is used to do the math operations using lambda functions 
#With the if elif statements the user can enter the operation they want to do and the function will return the result
#The main function is the function that runs the program and takes the user input 
#The user is asked to enter the operation they want to do and the numbers they want to do the operation on




def operate(operation, x, y):#this is the function that does the math operations
    add = lambda x, y: x + y
    subtract = lambda x, y: x - y#this is the lambda function that subtracts the numbers
    multiply = lambda x, y: x * y#this is the lambda function that multiplies the numbers
    modulus = lambda x, y: x % y
    exponent = lambda x, y: x ** y
    floating_point_division = lambda x, y: x / y
    integer_division = lambda x, y: x // y

    if operation in ['+', 'add', 'addition']:
        return add(x, y)
    elif operation in ['-', 'subtract', 'subtraction']:
        return subtract(x, y)
    elif operation in ['*', 'multiply', 'multiplication']:
        return multiply(x, y)
    elif operation in ['%', 'modulus', 'modulus division']:
        return modulus(x, y)
    elif operation in ['exponent', 'exponential', '^']:
        return exponent(x, y)
    elif operation in ['//', 'integer division']:
        return integer_division(x, y)
    elif operation in ['/', 'floating point division']:
        return floating_point_division(x, y)
    else:
        print("Invalid operation. Please try again.")


def main():
    operation = input("Enter an operation: ")
    x = int(input("Enter a number for x: "))
    y = int(input("Enter a number for y: "))
    result = operate(operation, x, y)
    print(result)

if __name__ == '__main__':
    main()
