#u67661285
#yUSRA rASOOL
import random as rand

# summary: this program is a magic 8 ball that answers questions and if the user wants to quit the program they can type no, and the program will end
#THE LIST OF ANSWERS ARE outputs that are printed with the random function,  TO ANY RESPONSE THAT IS NOT NO
#THEVOID FUNCTION IS THE FUNCTION THAT PRINTS THE ANSWER
# The use of random.randint() is to generate a random number between 0 and 19 to print the answer
#THE MAIN FUNCTION IS THE FUNCTION THAT RUNS THE PROGRAM AND KEEPS IT RUNNING IN A LOOP, ASKING THE USER FOR A QUESTION AND PRINTING THE ANSWER



def void(index):#this is the function which stores the list of answers and prints the answer
    answers =  ["it is certain","As I see it, yes", "Reply hazy, try again", "Don't count on it", "It is decidedly so", "Most likely", "Ask again later", "My reply is no", "Without a doubt", "Outlook good", "Better not tell you now", "My sources say no", "Yes - definitely", "Yes", "Cannot predict now", "Outlook not so good", "You may rely on it", "Signs point to yes", "Concentrate and ask again", "Very doubtful"]  
    print(answers[index])#this is the print statement that prints the answer

def main():
    while True:#this is the loop that keeps the program running
        question = input("Ask the magic 8 ball a question: ")#this is the input for the question
        if question.lower() == 'no':
            #this is the if statement that ends the program if the user types no
            break#this is the break statement that ends the program
        else:
            void(rand.randint(0,19))#this is the function that prints the  random answer if the question is not answered as no
      
        
main()#this is the function that runs the program and keeps it running in a loop