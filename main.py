


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

import random  #allows random selections in the program

#
def tell_joke(jokes):
    joke = random.choice(jokes)
    for line in joke:
        input(line)
        print(joke[-1])


def get_feedback():
    rate = int(input("Please rate our game 1-10: "))
    print(str(rate * 10) + " percent satisfaction rate")

    
    recommend = input("Would you reccomend this game to a friend?")
    if recommend in ["yes","maybe"]:
        print("Thanks, we appreciate it!")
    else:
        print("Sorry you didn't enjoy the game")


#added a list with the three different jokes

jokes = [
["Knock Knock,""Calder," "Calder police Ive been robbed!"],
["Knock Knock," "Tank," "You are welcome!"],
["Knock Knock," "Broken pencil," "Nevermind it's pointless!"]
]

answer = input("Do you want to hear a joke? ").lower()
while answer =="yes":
        print("Cool! I'll tell you one!")
        tell_joke(jokes)
        answer = input("Do you want to hear another joke (say yes) or are you finished (say finished) ?").lower()

if answer =="finished":
    get_feedback()
else:
     print("Okay thanks for nothing!")
    




















#EXTRA RANDOM CODE WE TRIED USING

# like_jokes = input("Do you like jokes?")
# while like_jokes == "yes":
#     print("Well howdy!")
#     print("I am quite the comidian")

# else:
#     double_check = ("Are you sure?")
#     if double_check == "yes":
#         print("Awww shucks, talk to you later :()")
#     else:
#         like_jokes == "yes"






































# ORIGINAL CODE JUST IN CASE:
# joke = input("Do you want to hear a joke? ")
# if joke == "no":
#     print("Okay suit yourself!")
# while joke == "yes":
#     print("Great, Let's Play")
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     if question == "robbers":
#         input("Knock Knock ")
#         input("Calder")
#         print("Calder police - I've been robbed!")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "tanks":
#         input("Knock Knock ")
#         input("Tank ")
#         input("You are welcome! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "pencils":
#         input("Knock Knock ")
#         input("Broken pencil ")
#         input("Nevermind, it's pointless! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
# if joke == "finished":
#     rate = int(input("Please rate our game 1-10! "))
#     final_score = int(rate * 10)
#     print(str(final_score) + " percent satisfaction rate")
#     friend = input("Would you recommend this game to a friend? ")

#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
#     else:
#         print("Sorry you did not enjoy it. ")