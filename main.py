# Performance task ready

joke_list = [
["Knock Knock", "Calder", "Calder police Ive been robbed!"],                                    # All three jokes are in this list
["Knock Knock", "Tank", "You are welcome!"],
["Knock Knock", "Broken pencil", "Nevermind it's pointless!"]
]

import random  

def tell_joke(joke_list):
    selected_joke = random.choice(joke_list)                                                         # selects a random joke in joke_list
    for joke in selected_joke:
        input(joke)
        print(joke[-1])
    
def get_feedback():
    rate = int(input("Please rate our game 1-10: "))                                        # after the user is finished they will give feedback
    print(str(rate * 10) + " percent satisfaction rate")                                # MATH     miltiplies answer by 10 to gewt a percentage. 
    recommend = input("Would you reccomend this game to a friend?")
    if recommend in ["yes","maybe"]:
        print("Thanks, we appreciate it!")
    else:
        print("Sorry you didn't enjoy the game")







# INPUT STARTS HERE

answer = input("Do you want to hear a joke? ").lower()                                   # Asks users if they want to hear a joke
while answer =="yes":                                                                    # WHILE LOOP: when answer is yes it'll give them a random joke and then ask if tehy want another of if they're finished
        print("Cool! I'll tell you one!")
        tell_joke(joke_list)
        answer = input("Do you want to hear another joke (say yes) or are you finished (say finished) ?").lower()

if answer =="finished":                                                                  # IF: They say finish then ask user for feedback
    get_feedback()

else:
     print("See you later!")                                                             # ELSE: They say "no" or anythinng else for hearing a joke it will print "See you later"
    




















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