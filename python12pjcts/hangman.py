import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses sometthing from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #whatt the user has guessed
    
    #getting user input
    while len(word_letters) > 0:
        #letters already used
        print('You have used these letters: ', ' '.join(used_letters))
        
        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
    
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print("You have used that character. Pick another character")
        
        else: 
            print("Invalid character. Try again")
hangman() 

user_input = input("Guess the word I am thinking: ")
print(user_input)

