import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    # get all the uppercase letter from the english dictionary from the string file
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 20
        
        
    while len(word_letters) > 0 and lives > 0:
            print(f"You have {lives} lives left")
            
            # ' '.join(['a', 'b', 'c']) => 'a b c'
            print("You have used: ", ' '.join(used_letters))
            
            # what current word is (ie -i-ch)
            current_word_list = [letter if letter in used_letters else '-' for letter in word]
            print("Current word: "," ".join(current_word_list))
            
            user_letters = input("Hangman: ").upper()
            if user_letters in alphabet - used_letters:
                used_letters.add(user_letters)
                if user_letters in word_letters:
                    word_letters.remove(user_letters)
                else:
                    lives = lives-1
            
            elif user_letters in used_letters:
                print("Invalid, you've guessed that letter before...")
            
            else:
                print("Invalid, please enter a valid character")
        
    if lives == 0:
        print("Game Over, you've killed the man!") 
    else:
        print("You've guessed the word!")  
    

hangman()
        