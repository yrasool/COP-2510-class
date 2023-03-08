x = 15 # global variable #global variable is defined outside the function #global variable can be used in any function

#---function definition---
def vofun1() :
    print(f"In vofun1, x is {x}") #global variable can be used in any function
def vofun2() :
    print(f"In vofun2, x is {x}") #global variable can be used in any function as long as x  is not defined as a local variable  x is a local variable here
    
def pythag(a,b) :
    c = (a**2 + b**2)**0.5
    return c

#---start --main function---
def main():
    vofun1() #output will be : In vofun1, x is 15
    x = 5 #local variable #local variable is defined inside the function #local variable can only be used in the function where it is defined
    print(x) #output will be : 5
    vofun2(10)#calling the function#10 is an argument# x = 10
    
a, b = input("Enter two numbers: ").split()  # split function splits the input into two strings with a space in between a nd b a = 3 b = 4
a = float(a)
b = float(b)

print(f"The hypotenuse is {pythag(a,b)}", end = " ") #calling the function #a and b are arguments #end = " " is used to print the output in the same line
#output will be : The hypotenuse is 5.0

#testing default arguments # calling printdate function with different number of arguments this will lead to execite prindate before tekkenstats
printdate(2,16)  #default argument
printdate(2,16,2024) #default argument with one argument passed in the function call
printdate(2,16,2025,3)#default argument with two arguments passed in the function call

#test function with keyword arguments

tekkenstats(gender = 'male', height = 180, name = "jin Kazama", age = 21) # this is a keyword argument # the order of the arguments does not matter
# the keyword argument must be defined in the function definition

def printdate(month,day,year = 2021, style = 1) :#default arguments#default arguments must be defined at the end of the function definition
    #default arguments must be defined at the end of the function definition
    if style == 1:
         print(f"{month}/{day}/{year}")
    elif style == 2:
        print(f"{month}-{day}-{year}")
    elif style == 3:
        print(f"{month}.{day}.{year}")
    else:
        print("Invalid style")
        
def tekkenstats( name,age,gender,height) : #notice the order of the arguments is different from the order of the keyword arguments in the function call, 
    #this is not a problem becuase the order of the arguments does not matter in the function call
     print(f"Name : {name}\n Age: {age}\n Gender :{gender}\n Height : {height}")
    
main()
#---end --main function---# the order of the functions will be main, vofun1, vofun2, pythag, printdate, tekkenstats
    
