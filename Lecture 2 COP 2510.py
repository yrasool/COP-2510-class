# while is used in situtaion when u dont know the amount of times you have to  do the command
#below we will  see the while controlled loop
i =1 # is is the loop controlled initialization
while i <= 15:
    print(f' is {i}')
    i = i +1 #update statement 
print()    
#Without the update statement we get an infinite loop with i is 1 getting repeated

#alternate version of this : Infinite loop with a break statement. #it works but not the most efficent way

j =1
while True:
    if j <= 15:
         print(f'j is {j}')
         j = j+1
    else:
        break
# method 1 is  better visibly than method 2
# for loop
for k in range(15):# it allows me to associate objects with container or ranges in python
    print(f'{k}',end ='')
print()    

for k in range (1,16):
    print(f'{k}',end='')
print()

for k in range(100,201,10):
    print(f'{k}', end= '')
print()    
# for loop with decrement
for k in range (1000,99,-50):
    print(f'{k}', end ='')
print()

n = int(input("how many times should I say 'Frolic'? :"))
for x in range (n):
    print("Frolic")
# for loop with string
plan = ' get some food after class.'
print(len(plan)) # return the size of the container
for p in plan:
    print(f'{p}', end = '-')
#for loop with lists    
names = ['Jinx', 'Vi', 5, 11, 'Caityn']    
for na in names :
     print(f' HI {na}!')
#In a hotel no one likes the 13th and 4th floor. I need to come with a process to iteerate over 20 floors in hotel,
#break in a for loop is shown here
for v in range (1,21): #   1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
     if v ==4 or v == 13: # if v is 4 or 13 then skip it
        continue   # continue to the next iteration # output is 1,2,3,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20  # break out of the loop # output is 1,2,3,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20   
        
print()
        
