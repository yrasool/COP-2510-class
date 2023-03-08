#==================function that accepts two parameters, and return a list===================

def multiples(v, a):
 mlist = []
 for m in range(1, va[1] + 1):
    mlist.append(m * va[0]) #append- add values to the end of the list
 return mlist
#__function that return a dictionary
def meaning():
 translate = {'ngl': 'not gona lie' , 'yet' : 'throw'}
 return translate
def faciorial(n):
 if n == 1 or n == 0:
    return 1
 else:
   return n * faciorial(n-1)

#lambra function - small anoymouse function
#can accept mulitpul paramters but only one expression
val = lambda x: x+5 #x
def main():
  value= int(input('Starting value?'))
  amt = int(input('Number of multiples?'))

#test function that returns a list

#print(f'The first {amt} multiples of {value} is {multiples(value, amt)}')
va= (value,amt)) # the
print(f'The first {amt} multiples of {value} is {multiples(value, amt)}')#THE OUTPUT IS THE SAME AS ABOVE

#==============no function definitions======================
main()

#test meaning function
#t= dict() #used to create an empty dictionary but not needed
t= meaning() #calling the function
print(f'here are some terms and there meanings {t}')#printing the dictionary

#test
number = int(input("enter a number>0:"))
print(f'{number}!={factorial}')

#cal lambda function (using input from before)
print(f'{number}+5= {val(number)}')
print(val) #printing the lambda exprestion not the value
#to use lambda function without an object, copy the function expresstion in the ()in IDLE shell and pass a value in ()

#
smallval = lambda a, b: a if a<=b else b

#
n1 , n2 =input("enter two numbers(sepated by a space):").split()
n1 , n2 = float(n1), float(n2)
print(f'The samll of {n1} and {n2} is {smallval(n1, n2)}')