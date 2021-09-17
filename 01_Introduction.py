def quiz_questions():
    return ""
                               
def instructions():
    print("**** How to Play ****")
    print()
    print(" You will start off with 5 points. For every question answered correctly you will gain 2 points."
    "For every question awnsered incorrectly you will lose 3 points. You will also be able to choose from three lifelines: ")
    print("50/50, where the answers will be cut down to two.")
    print("Flip the question, question will be changed.")
    print("Skip, the question will be skipped.")
    print("These lifeline can only be used once and do not cost any points. The objective of the game is to accumulate the most points.")
    print()
    return ""

def yes_no (question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response
        
        elif response == "no" or response == "n":
            response = "no"
            return response
        
        else:
              print("Please answer yes / no")



print("Welcome to the Sports Quiz!")
print() 
play_again = input("Press <Enter> to play....").lower()
print()
name = input("What is your name : ")
print("Hello " + name + "!")
played_before = yes_no ("Have you played the game before " + name + "? ")

if played_before == "no":
    instructions()

score = 5
question1 = "How many points is a free throw worth in basketball"
options1 = "a. 1\nb. 2\nc. 3\nd. 4\ne. 50/50\nf. Skip\ng. Flip Question"
print(question1)
print(options1)

while True:
    response = input("Hit 'a', 'b', 'c', 'd', 'e', 'f', 'g' for your answer\n")

    if response == "a":
        print("That is correct")
        score +=3
        print(""+ name + ", you have " + str(score) + " points")
        break
    
    elif response == "f":
        print(""+ name +", you have used the Skip Lifeline. This may not be used again. ")
        print(""+ name + ", you have " + str(score) + " points")
        break
    
    elif response == "g":
         print(""+ name +", you have used the Flip The Question Lifeline. This may not be used again. ")
         print(""+ name + ", you have " + str(score) + " points")
         break
    
    elif response == "e": 
        print(""+ name +", you have used the 50/50 Lifeline. This may not be used again. ")
        print("a. 1\nb. 2")

        
        

    else:
        print("Incorrect!!!. The correct awnser is a. 1 ")
        score -=2
        print(""+ name + ", you have " + str(score) + " points")
        break
  
        

     


