import random
import string
from words import words 

def is_valid_word(words):
    difficulty_input = input("Choose your difficulty: (X)Extreme  (H) Hard  (N) Normal  (E) Easy ").upper()
    if difficulty_input == "E":
        difficulty = 4
    elif difficulty_input == "N":
        difficulty = 5
    elif difficulty_input == "H":
        difficulty = 6
    elif difficulty_input == "X":
        difficulty = 9
    else:
        print("Invalid difficulty")
        
    while True:
        word = random.choice(words)
        if '-' not in word and ' ' not in word and len(word) == difficulty:
            return word.upper()

def hangboy():
    word = is_valid_word(words)
    word_letter = set(word)
    used_letter = set()
    alphabet = set(string.ascii_uppercase)
    lives = 8
    
    while len(word_letter) != 0 and lives != 0:
        print("You have guessed: ", " ".join(used_letter))
        print(f"You have {lives} more chances")
        current_word = [letter if letter in used_letter else '-' for letter in word]
        print("Word: ", ' '.join(current_word))
        user_letter = input("Hangman: ").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives = lives - 1
        else:
            print("You already guessed this letter, try another one!")
            
    if lives == 0:
        print(f"You lost! The word was {word}")
    else:
        print("Horray you did it!")
            
hangboy()