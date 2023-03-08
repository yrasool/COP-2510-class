#loop else 
#else is usually used in situtaion if it is false 

for i in range (1,5):# this is a for loop, the range is 1 to 5 but 5 is not included, the loop will run 4 times
    print(i)
else :            # this will run only after the for loop runs successfully, if the loop is interrupted by break or continue this will not run  
    print("Loop completed without interruptions") # this will print out because the loop is not interrupted by break or continue


#Loop else with break 
for i in range (1,5):
    print(i)
    break    # this interrupt the for loop and result is only 1 because of break
else :            # this should not execute because of break 
   print("Loop completed without interruptions")


#LOOp else with continue 
for i in range (1,11):
   if i == 4 :
        continue # this will skip the iteration of 4 and continue with the next iteration
        print(i)
else :            # this will run only after the for loop runs successfully  
 #   print("Loop complted without interruptions")




#nested loops  - for every 1 iteration of the outer lopp the ineer loop completes all  iterations 0--2, 0--3, 0--4, 0--5, 0--6
digit1 = 0
while digit1 <= 9 :#outer loop
    digit2 = 0 
    while digit2<= 9:#inner loop
        print(f"{digit1} -- {digit2}")
        digit2 += 1
    digit1+= 1 #notice indentation
    
# we can use walrus operator for outer loop as well, but we need to use a break statement to break the outer loop like below as shown in line 70
        
digit1 = 0
while digit1 <= 9 :#outer loop
    digit2 = 0
    #break # this loop will break #no output 
    while digit2<= 9:#inner loop
        print(f"{digit1} -- {digit2}")
        digit2 += 1
        #break   # the statement here will break the second the loop
    digit1+= 1 #notice indentation
    #break # a break statement here will interruot the outer while loop and we get a zero only for digit 1 

#effect of break on nested structure 

i = 7
while i < 15:
    if i == 7:
        break # the output will be 7 only because the break statement will break the loop and not print the rest of the numbers
    print(i)
    i += 2
    
    
    
#walrus operator and while loops #if we take parenthesis out  from line  we will see the "number is false" printed out.
# because with the one # parenthisis out the number inputed is first compared to being negative or positive and then assigned to NUmber .
# # WHich is why the whole operation after that is not considered  
#The third parenthisis allows us to store integer in the varaible NUmber and then compare it 

while(Number := int(input("Enter a positive number : "))) < 0: 
    number = int(input("invalid. Enter a new number that is positive :"))
    
print(f"Your number is {Number} ") 

#another method using continue
while(Number := int(input("Enter a positive number : "))) < 0: # this will ask for a number and if it is negative it will ask for another number
   continue # this will skip the print statement and ask for another number if the number is negative instead of if statement we can use continue
print(f"Your number is {Number} ")  # this will print the number if it is positive 


# below is
while(Number := int(input("Enter a positive number : "))) < 0: # this will ask for a number and if it is negative it will ask for another number
    print("invalid", end = '')      # this will print invalid and not go to the next line
print(f"Your number is {Number} ") 

 #contniue from lecture 5 cop 2510
#enumerate function in python guides us to the index of the item in the list
# m starts at 0 by default which means first item in list named m   
# 11th item in a list is not considered  hence 1 to 10 is considered in reality by the function
for m ,n in enumerate(range(1,11)):
    #print(f"{m}*{n} = {m*n}")  
   
#for m ,n in enumerate(range(21,31)):
    #print(f"{m}*{n} = {m*n}") 
    
# we have the ability to set the value of m the start means m starts at 1  
#for m ,n in enumerate(range(21,31),start = 1):
    #print(f"{m}*{n} = {m*n}")  