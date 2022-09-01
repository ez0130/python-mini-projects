import random
import time
from pic import stages, logo
import os
from words import word_list


print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

guessed_letter = []
display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    

    guess = input("Guess a letter: ").lower()
    os.system('CLS')
    
    
    
    if guess in display:
        print(f"You've already guessed {guess}")
    guessed_letter.append(guess)
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    print(f"{' '.join(display)}")


    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        
        if lives == 0:
            print(stages[lives])
            game_is_finished = True
            print("You lose. Word was", )
            print("do you want to know what was the answer?")
            a = input("Y or N?").lower()
            if a == "y":
                print("The answer is", chosen_word)
            time.sleep(10)
        
    if not "_" in display:
        game_is_finished = True
        print(print("Congrats! You have guessed the word correctly!"))
    print("guessed letter is ", guessed_letter)
    print(stages[lives])


    
