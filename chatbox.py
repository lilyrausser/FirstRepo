chatting = True
import random


name = input("Hi! My name is Lily! What is your name? ")

print("It is Great to meet you " + name + "!")

print("Make sure to use capital letters when typing responses.")

while chatting == True:
    user_ask = input("Type here:  ")
# use loops to confine questions
    if user_ask == "Hi":
        print("Hi " + name + "!")

    elif user_ask == "Yo":
        print("Yo, what's up, " + name + "!")
    elif user_ask == "What is your favorite color?":
        print("Green!")
    elif user_ask == "Do you follow sports?":
        print("Of course!! I love watching rowing, swimming, basketball, softball and gymnastics!")
    elif user_ask == "What is your favorite weather??":
        print("A nice 75 degrees, no wind. NO WIND.")
    elif user_ask == "What is your favorite show?":
        print("Parks and Rec")
    elif user_ask == "What is your favorite food?": 
        print("Easy, sushi!!")
    elif user_ask == "What is your favorite movie?": 
        print("I dont know if i have one!")
    elif user_ask == "What is your favorite movie genre?": 
        print("Either comedy or horror")
    elif user_ask == "What is your favorite song genre?": 
        print("EDM")
    elif user_ask == "What is your favorite place?": 
        print("home")
    elif user_ask == "Do you want to play a game?":
        print("Of course " + name + "!!")
        game()
    elif user_ask == "Quit":
        chatting = False
    else:
        print("Talk to me!")

    if chatting == False:
        break
print("It was nice talking to you!")

def game(): 
    word = ['blue', 'green', 'alabama', 'bright', 'mississippi'] 
    guess_word = ''
    store_letter = ''
    guess_count = 0
    guess_limit = 20

 
    print("Lets play the 'Guess that word game'!!! You have 20 guesses for the specified word.")
    print("Lets start!")
    print() #Check this
    while guess_count < guess_limit: 
        guess_letter = input('Guess a letter: ')
        guess_count += 1
        if guess_letter in word: 
            print('yes!')
            store_letter += guess_letter
        else: 
            print('nope!')
            guess_word = input('Guess the whole word: ')
        if guess_word.lower() == word: 
            print("Yay! Congradulations!")
        else: 
            print('Sorry! The answer was, ', word)
        input('Press Return to leave the program')

