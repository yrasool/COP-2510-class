#All about functions (collection of statements used for a specific purpose)
#---main function------
def main() : # main function #main function is defined by the user. 
    #it's not a built-in function. it's a function that the user creates. 
    # it's a function that the user creates to organize the code.
    fun1() # calling the function #the interperter will not show any output for this function but definition is necessary for the function to be called.
    #There will be an error if the function is not defined.
    y = int(input("Enter a number: "))#y is a variable that stores the input
    #return value of the function
    z = doubval(y) #y is an argument (variable,value or object used in function
    #call)#z is a variable that stores the return value of the function
    
#void function (doesn't return a value)
def fun1() : #function definition
    print("This is a void function") #this will be printed when the function is called , the output will be in the main function
    return        #returning back to the main function becuase no return value
# return here is exit point of the function.

#value returning function (returns a value)
def doubval(x) : #x is a parameter (variable used in function definition)
    return 2*x #return statement is the exit point of the function and it
#returns a value

#IN CASE OF DUPLICATE FUNCTION NAMES, THE RECENT DEFINITION FUNCTION  IS USED
def main():
    print("This is the second main function, this is the one that will be used")
#BEWARE OF CREATING FUNCTIONS WITH THE SAME NAME EVEN WITH DIFFERENT PARAMETERS
def doubval(a,b):
    return a*b

#--no function definitions after this line
main()
#calling the main function above
    
    
    
