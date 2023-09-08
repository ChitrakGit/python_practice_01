import random
import string
from words import words


# print(words)

def get_valid_words():
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_words()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 2
    print("########",word)
    while (len(word_letters) > 0) & (lives > 0):
        # used letters
        print("your life is ",lives,"used letters ", ' '.join(used_letters))
        # what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f"current is { ' '.join(word_list)}")
        user_letter = input("Guess a later --> ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if(user_letter in word_letters):
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in used_letters:
            print("You already guessed")
        else:
            print("Invalid Character !!!")

    if lives > 0:
        print(f"Congratulations. Word is {word}")
    else:
        print(f"Failed. Word is {word}")


hangman()
