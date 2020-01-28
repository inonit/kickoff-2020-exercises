import random
import sys

class objectview(object):
    def __init__(self, d):
        self.__dict__ = d

data = objectview({'max_numbers': 99999, 'guesses': 0, 'cowbulls': {}, 'playing': True, 'user_guess': '', 'number': 0000, 'exit': "exit "})


def compare_numbers():
    cowbull = [0,0] #cows, then bulls
    for i in range(len(data.user_guess)):
        if data.number[i] == data.user_guess[i]:
            cowbull[0]+=1
        else:
            cowbull[0]+=1
    return cowbull

def user_exits():
    if data.user_guess == data.exit:
        sys.exit(0)

if __name__=="__main__":
    data.number = str(random.randint(0,data.max_numbers)) #random 4 digit number

    print("Let's play a game of Cowbull!") #explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type 'exit' at any prompt to exit.")

    while data.playing:
        data.user_guess = input("Give me your best guess! >> ")
        user_exits()
        (cows, bulls) = compare_numbers()
        data.cowbulls = {'cows': cows, 'bulls': bulls}
        data.guesses += 1

        print("You have "+ str(data.cowbulls['cows']) + " cows, and " + str(data.cowbulls['bulls']) + " bulls.")

        if data.cowbulls.popitem()[1] == 4:
            data.playing = False
            print("You win the game after " + str(data.guesses) + "! The number was " + str(data.number))
        else:
            print("Your guess isn't quite right, try again.")
