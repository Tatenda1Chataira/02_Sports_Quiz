print("Mathematics Quiz")
question1 = "Who is president of USA?"
options1 = "a.Myslef\nb. His dad\nc. His mom\nd. Barack Obama\n"
print(question1)
print(options1)

while True:
    response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

    if response == "d":
        break
    else:
        print("Incorrect!!! Try again.")

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "d":
                stop = True
                break
            else:
                print("Incorrect!!! You ran out of your attempts")
                stop = True
                break
        if stop:
            break

# DO the same for the next questions of your round (copy-paste-copy-paste).
# At the end of the round, paste the following code for the bonus question.

# Now the program will ask the user to go for the bonus question or not