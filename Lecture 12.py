m = [1,2 ]
m *3
print(m*3)# multiply list

n =(4,5) #tuple and list are same here with numerical values in it 

print(n*4)

p =(8,9)#tuple
print(n +p)# add two tuple
q = (1)
print(q) # this is not a tuple because it is not iterable

q =(1,) # this is a tuple because it is iterable , it has a comma because it is a tuple and  will print the comma as well because it is a tuple
print(q)

print(n +q) # add tuple and list
# the output is (4, 5, 1) because tuple and list are different yet they can be added together because they are both iterable

name = "Yusra Rasool"

len(name) # length of string
print (f"the length of the string is {len(name)} , the lenthg is {len(name)} characters") # f string, # the length of the string is 12 , 
#the lenthg is 12 characters

#string slicing allows us to access a part of a string by referring to the index of the string
subname = name[0:3] # this will print the first three characters of the string # Yus is the output
print(subname)
#negative indexing is also allowed in string slicing
#-Ve indexing starts from the end of the string
print(name[-3]) # this will print the last three characters of the string # ool is the output#the output is l
print(name[-3:]) # this will print the last three characters of the string # ool is the output #the output is ool
print(name[-3:-1]) # this will print the last three characters of the string # ool is the output #the output is oo , _1 is not included and hence the last character is not included
#string slicing can be done with the step size
print(name [0:5:2]) # this will print the first five characters of the string with a step size of 2 # Ys is the output #the output is Ys
print(name [0:9:3]) # this will print the first nine characters of the string with a step size of 3 # Yr is the output #the output is Yr)
print(name [0:9:4]) # this will print the first nine characters of the string with a step size of 4 # Ys is the output #the output is Ys


#-----------------more about lists-----------------
names = ["John", "jake ", "jack", "george", "jenny", "jason", "jimmy", "joe","jim", [11,5]]


print(names[0][1])#this nested access will print the first character of the first element of the list # the output is o
#the nested approach will work for any number of nested lists
print(names[8][2])#this nested access will print the third character of the ninth element of the list # the output is e , 

names.insert(2,"BOb" ) #inserting an element at a specific index, the index is 2 and the element is Bob , the element will be inserted at index 2 and the rest of the elements will be shifted to the right
names.insert(5,"Kyle")#inserting an element at a specific index, the index is 5 and the element is Kyle , the element will be inserted at index 5 and the rest of the elements will be shifted to the right
names[-1].insert(0,12)#inserting an element at a specific index, the index is 0 and the element is 12 , the element will be inserted at index 0 and the rest of the elements will be shifted to the right
#we access the [11,5] list and insert 12 at index 0

names.append("Jennifer Aniston")#append will add the element at the end of the list
print(names) 

#to remove , use pop or remove 
names.pop()#this will remove the last element of the list,because no index is specified

names.pop(3)#this will remove the element at index 3, george will be removed
print(names)

#REMOVE will remove the first occurence of the element
names.remove("John")#this will remove the first occurence of the element John
print(names)


#--------------list comprehension----------------
#create a new list by modifying the elements of an existing list
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [i*i for i in list1]#this will create a new list by squaring the elements of list1

print(f"List1 is {list1} and list2 is {list2}")
#use list comprehension with a conditional (ternary) statement

list3 = [m/20 if m > 300 else m/20 for m in list2]#this will create a new list by dividing the elements of list1 by 20 if the element is greater than 300 and if the element is less than 300 then it will divide the element by 50
print(f"List1 is {list1}") 
print(f"list2 is {list2}")  
print(f"list3 is {list3}")

#you can use list comrephension with an if statement

list4 = [n-1 for n in list1 if n <= 2]#this will create a new list by subtracting 1 from the elements of list1 if the element is greater than 5 
print(f"LIst4 : {list4}") #if statement appears after the for loop


#using input statement to get user input
list5= [k -float(input("Enter a number: ")) for k in list1]#this will create a new list by subtracting the user input from the elements of list1

#----dictionary vs matchcase-------------------

month = input("enter month: ")
season = {"January": "Winter ", "February": "Winter", "March": "Spring", "April": "Spring", "May": "Spring", "June": "Summer", "July": "Summer", "August": "Summer", "September": "Autumn", "October": "Autumn", "November": "Autumn", "December": "Winter"}


print(f" In{month} we have {season.setdefault(month)} in Florida") #setdefault will return the value of the key if the key is present in the dictionary, if the key is not present then it will return none
#the output is InJanuary we have Winter  in Florida

#matchcase can be used in version 3.10 or higher 
season = "Winter"#this is the default value
#match case is used to match the value of a variable with a set of values
match month:#this will match the value of month with the values in the case
    case "January" :#if the value of month is January then the value of season will be Winter #
        season2 = "Winter"#this is used to assign a value to season2























