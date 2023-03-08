# Intro to Loops: Assignment 3 and Activity 4
# Date: 07/02 (derived from Yusra's code and recording from the same week)

# loop else (else can be used w for loops and while loops)
# the "else" clause is usually used in situations when the if condition is false

for i in range (1,5): # designed to run 4 times bc the stop value is exclusive in ranges
    print(i)
else :            # you can use else clauses w for loops. 
                  # else clauses with for loops run will run only after the for loop runs successfully and completes its intended iterations and doesn't have other instructions attached
    print("Loop completed without interruptions")

# potential else clause w for loop uses: organize data w/out having to create a separate if statement after the for loop

# loop else w break (a potential reason for the else clause w for to not execute bc the for loop doesn't run fully)

for i in  range (1,5):
    print(i)
    break # this causes the loop to end after one iteration 
else: # won't execute bc of break
    print("Loop completed without interruptions")

# loop else with continue

for i in range (1,11):
    if i == 4:
        continue # 4 is not printed bc of this
    print(i)
else: # take care to not associate this else statement w the if clause. it's associated w the for loop clearly bc of the indentation.
      # runs bc continue (skipping an iteration) is not considered an interruption in the for loop. skipping one or several iterations does not count as an interruption
    print("Loop completed without interruptions")

# nested loops: for every one iteration of the outer loop, the inner loop has to complete all iterations

digit1 = 0 # unlike a for loop which has a range variable located in the same line, while loops need loop control variable that is placed outside of the loop (???? why do we need this) (???? said sth about needing this unless she uses a walrus operator which she's deliberately leaving out rn)
# the loop control variable should be involved should be involved in three places: initialization, condition, and update
while digit1 <= 9: # outer loop
    digit2 = 0 # second loop control variable
    # break here would give us no output bc it breaks the outer loop
    while digit2 <= 9: # inner code
        print(f"{digit1} -- {digit2}") # the hyphens have no meaning except to distinguish b/w digits 1 and 2 in echo printing
        digit2 += 1
        break
        # break here would break only the second loop. the break staetment in python isn't powerful enough to break all nested loops unless it's in the outer level. 
        # the outer loop would still run without incident
    digit1 += 1
    # break here would interrupt the outer while loop after 1 iteration and the inner loop is still able to complete all its iterations while digit 1 is 0

# variation (my own)

# digit1 = 0 # unlike a for loop which has a range variable located in the same line, while loops need loop control variable that is placed outside of the loop (???? why do we need this) (???? said sth about needing this unless she uses a walrus operator which she's deliberately leaving out rn)
# # the loop control variable should be involved should be involved in three places: initialization, condition, and update
# while digit1 <= 9: # outer loop
#     digit2 = 0 # second loop control variable
#     print(f" this is {digit1}")
#     continue
#     while digit2 <= 9: # inner code
#         print(f"{digit1} -- {digit2}") # the hyphens have no meaning except to distinguish b/w digits 1 and 2 in echo printing
#         digit2 += 1
#         # break here would break only the second loop. the break staetment in python isn't powerful enough to break all nested loops unless it's in the outer level. 
#         # the outer loop would still run without incident
#     digit1 += 1

# in this case, the outer while loop will be infinite bc the continue statement skips the rest of the code for every iteration and digit1 is never updated 



# the point of the nesting example is to show that the inner loop runs through all its iterations or is interrupted before the second iteration of the outer loop begins

# collectively as a nested structure, the nested loop (without any breaks) runs 10*10 = 100 times

# like you can create while loops in a nested structure, you can create a for loop in a nested structure as well.

# --------- enumerate function: allows to get two values at once instead of one ---------------
# used w loops that have ranges or w containers e.g lists, dictionaries, tuples, etc.
# you can call on two range variables
# relies on objects w components that can be counted like dictionaries, list, ranges, etc.

for m, n in enumerate(range(1,11)):
    print(f"{m}*{n} = {m*n}")

# n represents the range variable for values. starts at 1 and ends at 11. 
# m represents the range variable for position. starts at 0 and ends w 9 bc i is giving us the index at which those values would be contained. 
# starts w 0 bc the index for positions in python starts at 0 instead of 1


