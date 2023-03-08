from PIL import Image

# local dictionary {key: value}
animals = {'dog': 'bark', 'cat': 'meow', 'cow': 'moo'}

# function to access the specific value of the key
def rename(ani):
    for k in ani:
        print(f'animal: {k}\t\tsound: {ani[k]}')

# function to print the list of esport games
def esportgames():
    # declare a local list
    games = ['Dota 2', 'Fortnite', 'League of Legends', 'Counter Strike: Global Offensive']

    for (index, element) in enumerate(games): #enumerate is a function that returns a tuple
        print(f'{index + 1}. {element}')
    print()

    # to print the elements of the list in reverse order
    rank = 4  # this is a variable
    for i in reversed(games):  # i will be an element
        print(f'{rank}. {i}')
        rank -= 1

    # to access the elements of the list
    print(games[0])  # this will give Dota 2
    print(games[1])  # this will give Fortnite


# function to demonstrate working with images
def image_function():
    image1 = Image.open('C:/Users/yusra/OneDrive - University of South Florida/Pictures/FAMILY/IMG_5120.JPG')
    image1.show()
    
#working with images below
#image1.show()
#show image with function
#showpic(image1)


#create a thumbnail
image2 = Image.open('C:/Users/yusra/OneDrive - University of South Florida/Pictures/FAMILY/IMG_5120.JPG')
image2.thumbnail((250, 250))  # this will resize the image to 250x250 # this will save the image to the current directory
#a tuple is a list that cannot be changed, a tuple is a container that holds multiple items,
# inner parenthesis is needed for tuples but not for lists and is optional for tuples
#image2.save("minigw4.png")

#show the thumbnail
#showpic(image2)

value = int(input("Starting value: "))
amt = int(input("Number of multiples: "))

print(f'The first {amt}of {value}  is {multiples(value,amt)}
va = (value, amt)
print(va[0])
    


def showpic(img):#img will be an image object the function will take an image object as a parameter
    #show the image
    img.show()
    
#function that accepts two parameters and returns a list
def multiples(a, b):
    mlist = []#this is a local list#mlist will be a list
    for m in range(1, b + 1):#range is a function that returns a list#range(1, 5) will give [1, 2, 3, 4]
        mlist.append(a * m)#this will append the multiples of a to the list#append is a method that adds an element to the end of a list
    return mlist#this will return the list
    




def main():
    print("Here are some of the most popular esport games in the world")
    esportgames()

    # to access the specific value of a key in a dictionary
    print(animals['dog'])  # this will give bark
    print()
    rename(animals)  # this will give animal: dog	sound: bark

    # to demonstrate working with images
    image_function()


main()
#I moved the rename function above the esportgames function since the former was being called inside the latter, 
# and Python needs the function to be defined before it can be called. I also added a image_function function to 
# demonstrate working with images. Additionally, I added comments to explain what each part of the code is doing.
