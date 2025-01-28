import random

# Create Display Images of Hangman Game:


def hangman_display(list):
    """Prints a list out row by row. Input the list of hangman display rows"""
    for row in list:
        print(row)


row0 = '          []=========]       '
row1 = '          ||         |       '
row2full = '          ||         O       '
row3full = '          ||  =====--H--====='
row4full = '          ||         H       '
row5full = '          ||         H       '
row6full = '          ||       -----     '
row7full = '          ||       |   |     '
row8full = '          ||       |   |     '
row9full = '          ||      _|   |_    '
row10 = '          ||                 '
row11 = '======================       '

row7_one_leg = '          ||       |         '
row8_one_leg = '          ||       |         '
row9_one_leg = '          ||      _|         '

row7_no_leg = '          ||                 '
row8_no_leg = '          ||                 '
row9_no_leg = '          ||                 '

row3_one_arm = '          ||  =====--H--     '

row3_no_arm = '          ||       --H--     '

row3_no_body = '          ||                 '
row4_no_body = '          ||                 '
row5_no_body = '          ||                 '
row6_no_body = '          ||                 '

row2_no_grape = '          ||                 '

fully_hung = [row0, row1, row2full, row3full, row4full, row5full, row6full, row7full, row8full, row9full, row10, row11]
one_leg = [row0, row1, row2full, row3full, row4full, row5full, row6full, row7_one_leg, row8_one_leg, row9_one_leg, row10, row11]
two_arms = [row0, row1, row2full, row3full, row4full, row5full, row6full, row7_no_leg, row8_no_leg, row9_no_leg, row10, row11]
one_arm = [row0, row1, row2full, row3_one_arm, row4full, row5full, row6full, row7_no_leg, row8_no_leg, row9_no_leg, row10, row11]
head_and_body = [row0, row1, row2full, row3_no_arm, row4full, row5full, row6full, row7_no_leg, row8_no_leg, row9_no_leg, row10, row11]
head = [row0, row1, row2full, row3_no_body, row4_no_body, row5_no_body, row6_no_body, row7_no_leg, row8_no_leg, row9_no_leg, row10, row11]
empty = [row0, row1, row2_no_grape, row3_no_body, row4_no_body, row5_no_body, row6_no_body, row7_no_leg, row8_no_leg, row9_no_leg, row10, row11]

display_progression = [[empty, head, head_and_body, one_arm, two_arms, one_leg, fully_hung], [empty, head, head_and_body, one_arm, two_arms, one_leg, fully_hung]]


# Define Functions
def user_guess(prompt, user):
    """Only lets the user input a valid guess"""
    global alphabet
    global already_guessed
    global invalid_character
    x = 0
    y = 0
    z = 0
    print(prompt)
    while x != 1:
        inpt = input().upper()
        try:
            if inpt in available_letters[user]:
                return inpt
            elif inpt in alphabet:
                if y == 0:
                    print(already_guessed)
                    y += 1
            else:
                if z == 0:
                    print(invalid_character)
                    z += 1
        except:
            x = 0


#AI_Letter_Guesses.txt

def automated_guess(user):
    """Returns a random-random letter in the alphabet
    based on each letter's frequency of appearance in
    the English Language"""
    x = 0
    letter_distribution = open('AI_Letter_Guesses.txt', 'r')
    letter_guess_list = letter_distribution.readlines()
    letter_distribution.close()
    for i in range(len(letter_guess_list)):
        letter_guess_list[i] = letter_guess_list[i].strip('\n')
    while x != 1:
        random_letter = random.choice(letter_guess_list)
        try:
            if random_letter in available_letters[user]:
                return random_letter
        except:
            x = 0


def opening_page(x=None):
    global root
    title = 'Ultimate Hangman'
    enter_to_cont = '...Press Enter...'
    print(title)
    print(enter_to_cont)
    input()


def game_menu(x=None):
    x = 0
    menu_text = 'Select a Game Mode\n' \
                '(1) Single Player\n' \
                '(2) Two Player'
    print(menu_text)
    while x != 1:
        num_players = input()
        try:
            if (int(num_players) == 1) or (int(num_players) == 2):
                return num_players
        except:
            x = 0


def game_theme(x=None):
    x = 0
    theme_text = 'Select a Theme\n' \
                 '(1) Merry Christmas!\n' \
                 '(2) Sports'
    print(theme_text)
    while x != 1:
        theme = input()
        try:
            if (int(theme) == 1) or (int(theme) == 2):
                return theme
        except:
            x = 0


def begin_game(x=None):
    begin_text = 'Press Enter to Begin'
    print(begin_text)
    input()


def random_word(theme_index: str):
    file = open(f'{theme_files[theme_index]}', 'r')
    theme_words = file.readlines()
    file.close()
    random_phrase = random.choice(theme_words)
    # random_phrase = random_phrase.strip()
    # random_phrase = random_phrase.split()
    return random_phrase


def nested_list(phrase):
    for word in phrase:
        letters = []
        for letter in word:
            letter = letter.upper()
            letters.append(letter)
        phrase[phrase.index(word)] = letters
    return phrase


def underscore(phrase):
    phrase = phrase.strip()
    word_list = phrase.split()
    shrowded_phrase = ""
    for word in word_list:
        for letter in word:
            shrowded_phrase += '_'
        shrowded_phrase += " "
    shrowded_phrase = shrowded_phrase.strip()
    return shrowded_phrase


def phrase_string(phrase):
    save_phrase = ""
    for word in phrase:
        for letter in word:
            save_phrase += letter
        save_phrase += " "
    save_phrase = save_phrase.strip()
    return save_phrase


def one_turn(player: int, special_phrase, display_phrase):
    global guess_prompt
    global turn_counter
    letter_display = " ".join(available_letters[player])
    print()
    print(f'player {player + 1}:')
    hangman_display(display_progression[player][image_indexes[player]])
    print(f'Lives: {lives[player]}')
    print(f'Available Letters: {letter_display}')  # Create a better display using loops and printing statements
    print(display_phrase[player])
    guess_prompt = 'Guess a letter'
    guess = user_guess(guess_prompt, player)
    # Decide if letter is valid guess
    # if guess in available_letters[player]:
    available_letters[player].remove(guess)
    if guess in special_phrase[player]:
        # Change Masked List to show the guessed letter
        for letter in special_phrase[player]:
            if guess == letter:
                display_phrase[player] = display_phrase[player][0:special_phrase[player].index(letter)] + letter + display_phrase[player][special_phrase[player].index(letter) + 1:]
                special_phrase[player] = special_phrase[player].replace(letter, " ", 1)
    else:
        image_indexes[player] += 1
        lives[player] -= 1
    # else:
    #     if guess in alphabet:
    #         guess_prompt = already_guessed
    #         turn_counter += 1
    #     else:
    #         guess_prompt = invalid_character
    #         turn_counter += 1
    masked_phrase_display = masked_phrase[player]
    hangman_display(display_progression[player][image_indexes[player]])
    print(masked_phrase_display)
    print(f'{lives[player]} Lives Left')
    turn_counter += 1


def AI_turn(player: int, special_phrase, display_phrase):
    global AI_letter_display
    global turn_counter
    global guess_prompt
    letter_display = " ".join(AI_letter_display)
    print()
    print(f'Player {player + 1}:')
    hangman_display(display_progression[player][image_indexes[player]])
    print(f'Lives: {lives[player]}')
    print(f'Available Letters: {letter_display}')  # Create a better display using loops and printing statements
    print(display_phrase[player])

    print(guess_prompt)
    guess_prompt = 'Guess a letter'
    guess = automated_guess(player).upper()
    # Decide if letter is valid guess
    # if guess in available_letters[player]:
    available_letters[player].remove(guess)
    if guess in special_phrase[player]:
        # Change Masked List to show the guessed letter
        for letter in special_phrase[player]:
            if guess == letter:
                display_phrase[player] = display_phrase[player][0:special_phrase[player].index(letter)] + "*" + display_phrase[player][special_phrase[player].index(letter) + 1:]
                special_phrase[player] = special_phrase[player].replace(letter, " ", 1)
    else:
        image_indexes[player] += 1
        lives[player] -= 1
    # else:
    #     if guess in alphabet:
    #         guess_prompt = already_guessed
    #         turn_counter += 1
    #     else:
    #         guess_prompt = invalid_character
    #         turn_counter += 1
    masked_phrase_display = masked_phrase[player]
    hangman_display(display_progression[player][image_indexes[player]])
    print(masked_phrase_display)
    print(f'{lives[player]} Lives Left')
    turn_counter += 1


# Define Variables
theme_files = {'1': 'Christmas_word.txt', '2': 'sports.txt'}
available_letters = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                       'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                       'U', 'V', 'W', 'X', 'Y', 'Z'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                       'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                       'U', 'V', 'W', 'X', 'Y', 'Z']]
AI_letter_display = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                     'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
turn_counter = 0
lives = [6, 6]
image_indexes = [0, 0]
already_guessed = 'You already guessed that letter,try again'
invalid_character = 'Input is Invalid'
turn = turn_counter % 2
guess_prompt = 'Guess a letter'
# Open an image
# with separater
printletters = " ".join(available_letters[turn])
#############################


#############################

# Display Title Page

# Take input to open the game menu
opening_page()

# opening_page()

#############################
# Take input for 1 or 2 players
players = game_menu()


# if 1 player *********************

# Decide which theme to play
theme_index = game_theme()

# Let user choose to begin game
begin_game()
# if 2 player *********************
#  theme_index = game_theme()
#   begin_game()


# Choose Random Word
secret_phrase = random_word(theme_index)
secret_phrase = secret_phrase.strip().upper()
secret_phrase = [secret_phrase, secret_phrase]


# Split that word / phrase into its letters
# secret_phrase = [nested_list(secret_phrase), nested_list(secret_phrase)]
save_phrase = (secret_phrase[:1])[0]
# phrase_string(secret_phrase[turn])
# Create Matching list with underscores instead of letters

masked_phrase = [underscore(secret_phrase[0]), underscore(secret_phrase[1])]


# Plays Game

if players == '2':
    while (lives[0] > 0) and (lives[1] > 0):
        if (masked_phrase[0] == save_phrase) or (masked_phrase[1] == save_phrase):
            break
        for i in range(2):
            # one turn defined as a function
            one_turn(turn_counter % 2, secret_phrase, masked_phrase)
    if lives[0] > lives[1]:
        winner = 'Player 1 Wins!'
    elif lives[0] < lives[1]:
        winner = 'Player 2 Wins!'
    else:
        winner = "It's a Draw!"
    print(winner)
    print(f'The secret phrase was {save_phrase}')
    masked_phrase_display = masked_phrase[turn]
else:
    while (lives[0] > 0) and (lives[1] > 0):
        if (masked_phrase[0] == save_phrase) or (masked_phrase[1] == save_phrase):
            break
        for i in range(2):
            # one turn defined as a function
            if turn_counter % 2 == 0:
                one_turn(turn_counter % 2, secret_phrase, masked_phrase)
            else:
                AI_turn(turn_counter % 2, secret_phrase, masked_phrase)
                break
    if lives[0] > lives[1]:
        winner = 'Player 1 Wins!'
    elif lives[0] < lives[1]:
        winner = 'Player 2 Wins!'
    else:
        winner = "It's a Draw!"
    print()
    print()
    print(winner)
    print(f'The secret phrase was {save_phrase}')
    masked_phrase_display = masked_phrase[turn]
