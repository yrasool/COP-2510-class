    
# while is used in situtaion when u dont know the amount of times you have tp do the command
#below we will  see the while controlled loop

#method 1
i =1 # is is the loop controlled initialization
while i <= 15:
    print(f' is {i}')
    i =+1 #update statement #THIS IS IMPORTANT FOR EVERY WHILE LOOP TO AVOID INFINITE LOOP
print()    #without  this print statement we get an infinite loop with i is 1 gettong repeated
#Without the update statement we get an infinite loop with i is 1 gettong repeated

#alternate version of this : Infinite loop with a break statement. #it works but not the most efficent way


#METHOD 2
j=1
while True:
    if j <= 15:
         print(f'j is {j}')
         j =+1
    else: #the else statement is here to avoid infinite loop, this will run after the if statement is false i.e j>15, when j>15 the else statement will run and break the loop
        break #THIS BREAK IS HERE TO AVOID INFINITE LOOP 
# method 1 is  better visibly than method 2

# for loop is used for repetition of a command a known number of times and it is better to avoid infinite loops
for k in range(15):# in allows me to associate objects with container or ranges in python #15 is the upper bound and 0 is the lower 
    #bound deafult #  15 is exlusive so it will print 0 to 14
    print(f'{k}',end ='') #
    print(f'{k},', end='') # this is better than the above line because it has a comma after the number which will show the output as 0,1,2,3,4,5,6,7,8
print() # this is to print a new line    

for k in range (1,16): #range is a function that returns a list of numbers,# range(1,16) is a list of numbers from 1 to 15
    print(f'{k}',end='') #end='' is used to print on the same line
print()# this is to print a new line  # this print function is important to print a new line after the above print function  
   
