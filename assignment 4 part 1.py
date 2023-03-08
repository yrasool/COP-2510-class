#question 1
#U67661285
#Yusra Rasool

#In the below code, the function power() is recursive. #The function power() takes two arguments, x and n. #The function power() returns x raised to the power of n. 
# #The function power() is recursive. #The function power() takes two arguments, x and n. #The function power() returns x raised to the power of n.
# the main function is the function that runs the program and takes the user input with the while loop to make sure the user enters a number between 2 and 50
def power(x, n): #this is the function that takes the base and the exponent and returns the base raised to the power of the exponent
    if n == 1 or n ==0: #this is the base case that returns the base if the exponent is 0 or 1
        return x #this is the base case that returns the base if the exponent is 0 or 1
    else:
        return x * power(x, n - 1) #this is the recursive function that multiplies the base by itself the number of times the exponent is

def main(): #
    base = int(input("Enter the base: "))
    exponent = int(input("Enter a whole number between 2 and 50: "))
    while exponent < 2 or exponent > 50:
        exponent = int(input("Invalid. Please enter a whole number between 2 and 50: "))
    result = power(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}")

if __name__ == "__main__": #this is the function that runs the program and takes the user input with the while loop to make sure the user enters a number between 2 and 50
    main() #this is the function that runs the program and takes the user input with the while loop to make sure the user enters a number between 2 and 50







    
    
    
