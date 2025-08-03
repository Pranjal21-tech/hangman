import random
from hangmans_word import word_list
from hangmans_art import stages, logo
#user ko 6 lives dega
lives = 6
print(logo)
chosen_word = random.choice(word_list) #genrate random words from word_list
print(chosen_word)
placeholder = ""
word_length = len(chosen_word) #it will store the length of chosen word
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder) #jitne chosen word ki length hogi utne underscore print kr dega
game_over = False #means game abhi over nh hua h
correct_letters = []
while not game_over:
    print(f"**************************** {lives} /6 LIVES LEFT****************************")
    guess_word = input("Guess a letter: ").lower()  #it will take input from user and store the  guessed letter in guess_word

    if guess_word in correct_letters:
        print(f"YOU HAVE ALREADY GUESSED {guess_word}") #it will indicate the user that he already guessed this letter using f string

    display = "" #it will show the guessed letters
    for letter in chosen_word:
        if letter == guess_word:
            display += letter
            correct_letters.append(guess_word) # if guessed_word in chosen word then it will add guessed word in correct_letters
        elif letter in correct_letters: #ye tab chlega jab if wrong hoga
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)
    
    if guess_word not in chosen_word:
        print(f"THE LETTER YOU GUESSED {guess_word} IS WRONG ")
        lives -= 1 # if the user guessed wrong letter 1 live will be reduced from left lives everytime
        if lives == 0:
            game_over = True # when lives is equal to zero game_over condition will true so the game will over
            print(f"***********************YOU LOSE, THE CORRECT WORD IS {chosen_word}**********************")
            
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    print(stages[lives]) # it will print the stage of a hangman
