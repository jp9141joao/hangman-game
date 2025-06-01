import random
import os

# Main function for the Hangman game
def Game(word):
    size = len(word)
    attempts = random.randint(6, 11)  # Random number of attempts between 6 and 11
    characters = []  # List to store the characters of the word
    layout = []  # List to display the current state of the guessed word
    checked = []  # List to store the letters already guessed
    correct_guesses = 0
    mistakes = ''  # String to store incorrect guesses

    # Initialize the layout with underscores or spaces
    for i in range(size):
        if word[i] == ' ':
            layout.append(' ')
            characters.append(word[i])
            correct_guesses += 1
        else:
            characters.append(word[i])
            layout.append("_ ")

    # Game loop: runs until the player guesses the word or runs out of attempts
    while correct_guesses != size and attempts != 0:
        os.system('cls')  # Clear the console for better visualization
        string_layout = ' '.join(layout)
        print(f'* Hangman *\nHint: Marvel and DC Character\nMistakes: {mistakes}\nRemaining attempts: {attempts}\n\n\n{string_layout}')
        
        resp = str(input('\nEnter a letter: ')).upper()
        while len(resp) != 1:
            resp = str(input('\nEnter a single letter: ')).upper()

        # Check if the guessed letter has not been checked before
        if resp not in checked:
            for i in range(size):
                if resp == characters[i]:
                    layout[i] = f'{characters[i]} '
                    correct_guesses += 1
                    checked.append(resp)

        # If the guessed letter is not in the word
        if resp not in characters:
            mistakes += f'{resp} '
            attempts -= 1  

    os.system('cls')  # Clear the console before showing the final result

    # Check if the player won or lost
    if attempts == 0:
        print(f'* Out of attempts *\nAnswer: {word}\nGame Over')
    else:
        string_layout = ' '.join(layout)
        print(f'\nYou did it!\n* Hangman *\n{string_layout}\nGame Over!')


# Reading the word bank from the file
word_bank = []
with open("hangman.txt", 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        word_bank.append(line)

# Main game loop: keeps running until the user chooses to exit
while True:
    i = random.randint(0, len(word_bank) - 1)  # Random index for the word
    word = word_bank[i].upper()
    Game(word)

    continue_game = int(input('\n* Do you want to continue? *\n1- Yes\n2- No\nAnswer: '))
    while continue_game != 1 and continue_game != 2:
        continue_game = int(input('* Do you want to continue? *\n1- Yes\n2- No\nAnswer: '))
    
    if continue_game == 2:
        print('Program Terminated!')
        break
