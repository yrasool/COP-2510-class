student = { "name ": "John", "age ": 25, "courses ": ["Math", "CompSci"]}
print(student["name "])#this will return the value of the key "name"
print(student.get("name "))#get method is safer than the first one
print(student.get("phone ", "Not Found"))#if key is not found, it will return the second argument

#returning a dictinonary from a function
def build_person(first_name, last_name):#function that takes two arguments
    person = {"first": first_name, "last": last_name}
    return person

musician = build_person("jimi", "hendrix")#calling the 
#function#and storing the returned value in a variable
#called musician and printing it
print(musician)

#returning a dictionary from a function with an optional argument
def build_person(first_name, last_name, age=""):#function that takes three arguments,#the age argument is optional
    person = {"first": first_name, "last": last_name}
    if age:#if age is not empty
        person["age"] = age#add the age to the dictionary
    return person #return the dictionary#the age argument is optional

jimi = build_person("jimi", "hendrix", 27)#calling the function,#storing the returned value in a variable called jimi and printing it#the age argument is optional
print(jimi)

#print factorials of numbers 
#5! = 5*4*3*2*1=120

#An iterative solution uses a loop to solve the problem
def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial
#the above code will return 120  if we put  n = 5 because 5! = 5*4*3*2*1=120
#getFactorial is a function that takes one argument

#A recursive solution uses a function to solve the problem
#A recursive function is a function that calls itself
#A recursive function must have a base case and a recursive case

def getFactorial(n): #getFactorial is a function that takes one argument
 if n < 2 : #base case
    return 1
 else:
    return n *getFactorial(n-1)

getFactorial(5)#calling the function and printing the result\
#the above code will return 120  if we put  n = 5 because 5! = 5*4*3*2*1=120

#it is important to stop the recursion at some point
#because if we don't stop the recursion, it will go on forever
#there has to be  base limit in the recursion fucntion or the program will run infinetly
import sys #importing the sys module#this module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter
sys.setrecursionlimit(10000)
#this will set the recursion limit to 10000
#the limit is 100 meaning that the recursion will stop after 100 iterations
getFactorial(2000)
#this will not work because the recursion limit is 1000


#the lambda keyword is used to create small anonymous functions
#A lambda function can take any number of arguments, but can only have one expression
def add(a, b):
    result = a + b
    return result
add(3,4)
#the above is the usual way of defining a function

#the same function can be defined using lambda
adding = lambda(y, z): y + z
adding(3,4)

plus = lambda x: x + 100
print(plus(50))

(lambda v, w : v*w)(3,4)#this is a single line function of two arguments
product = lambda c, d, e : c*d*e
print(product(3,4,5)) 


blah = lambda k,l = 15, m = 20 : k + l + m
print(add(20))#this will return 55#because k = 20, l = 15 and m = 20
#20 will be assigned to k and 15 and 20 will be assigned to l and m respectively
#this is because the default values of l and m are 15 and 20 respectively
multi = lambda *args : sum(args) #the args is a tuple here and the sum function will add all the elements in the tuple
#the use of tuple i to make the function more flexible and to accept any number of arguments
print(9,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
#this will return 190#because the sum of all the numbers is 190
higher_order = lambda x, func : x + func(x)
#the higher_order function takes two arguments, x and function func and returns the sum of x and the function func
higher_order(8, lambda x : x * x)
#this will return 72#because 8 + 64 = 72
#func x will be 64 because x = 8 and x * x = 64

(lambda x : (x%2 and "odd" or "even"))(3)# 3  is argument and the function will return odd

sub_string = lambda string : string in "Mama is here  "
#ths function will return true if the string is in the string Mama is here
#the above is a check if a string is a substring of another string
print(sub_string("Mama"))#this will return true
print(sub_string("Yusra"))#this will return false

#FIlter function using lambda

num = [1,2,3,4,5,6,7,8,9,10]
greater_than_5 = list(filter(lambda x : x > 5, num))
print(greater_than_5)#this will return [6, 7, 8, 9, 10]
#filter is a function that takes two arguments, a function and an iterable
#filter a list of numbers divisible by 4
list = [1,2,3,4,5,6,7,8,9,10]
divide = list(filter(lambda x : x%4 == 0, list))
print(divide)#this will return [4, 8]

list1 = [1,2,3,4,5,6,7,8,9,10]
double = list(map(lambda x : x*2, list1))
#the use of map here is to double the elements in the list
#without map, we would have to use a for loop to double the elements in the list
#the output will be [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

list3 = [3,4,5,6,7,8,9,10]
cube = map(lambda x : x**3, list3)
list(cube)#this will return [27, 64, 125, 216, 343, 512, 729, 1000]
#the use of map here is to cube the elements in the list


#reduce function using lambda in python allows us to reduce a list to a single value
from functools import reduce
list4 = [2,5,10,6,4,12]
sum = reduce(lambda x, y : x + y, list4)
#the above code will return 39 because 2 + 5 + 10 + 6 + 4 + 12 = 39
print(sum)#this will return 39)]

def quadratic(f,g,h):
    return lambda x : f*x**2 + g*x + h
j = quadratic(2,3,-5)
print(j(0))#this will return -5
print(j(1))#this will return 0




        