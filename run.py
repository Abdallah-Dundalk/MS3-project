import random

# ist containign 25 full stops that will be sliced into 5 rows for
# printing boards
board_list = []

# 4 random samples are taken from this list and used for the
# target ship coordinates.
computer_ship_locations = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                           [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                           [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                           [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                           [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]
                           ]

# list of 4 ships coordinates targeted by player.
new_cpu_ship_locations = []

# list of 4 ships coordinates targeted by CPU.
player_ship_locations = []

# These lists are used to print rows for cpu board.
list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []

# These lists are used to to print rows for players board.
player_list_1 = []
player_list_2 = []
player_list_3 = []
player_list_4 = []
player_list_5 = []

# These variables contain players scores.
PLAYER_SCORE = 0
CPU_SCORE = 0

# This variable stores the players name
player_name = []

# list of all guesses made by player
player_guesses = []


# list of all guesses made by CPU
cpu_guesses = []


def reset_game_values():
    """
    Clears all game values and resets scores to zero.
    """
    player_guesses.clear()
    cpu_guesses.clear()
    player_ship_locations.clear()
    board_list.clear()
    new_cpu_ship_locations.clear()
    player_name.clear()
    list_1.clear()
    list_2.clear()
    list_3.clear()
    list_4.clear()
    list_5.clear()
    player_list_1.clear()
    player_list_2.clear()
    player_list_3.clear()
    player_list_4.clear()
    player_list_5.clear()
    global PLAYER_SCORE
    global CPU_SCORE
    PLAYER_SCORE = 0
    CPU_SCORE = 0


def intro_msg():
    """
    Prints welcome message to terminal
    """
    # I borrowed this idea for multiplying character from Code Institute,
    # # I had been typing each character previously.
    print("-" * 70)
    print("This is BATTLESHIPS - MAN V MACHINE")
    # This wording is taken directly from the code institute Battleships game
    # as it is the most concise way to orientate the player
    print("Board size: 5. Number of ships: 4")
    print("Top left corner is row: 0, col: 0")
    print("-" * 70)


def add_name():
    """
    Prompts user to enter name
    """
    name = str(input("Enter your name to begin:\n"))
    player_name.append(name)


def generate_list():
    """
    Generates a list of 25 full stops that will be used by
    another function to create player boards
    """
    for x in range(25):
        board_list.append(".")
    return board_list


def print_cpus_board(list):
    """
    Slices a list of full stops before printing 5 lists to represent
    computers player board.
    """
    slice_1 = list[0:5]
    list_1.extend(slice_1)
    slice_2 = list[5:10]
    list_2.extend(slice_2)
    slice_3 = list[10:15]
    list_3.extend(slice_3)
    slice_4 = list[15:20]
    list_4.extend(slice_4)
    slice_5 = list[20:25]
    list_5.extend(slice_5)
    print("\nCPU Player Board:")
    print('  '.join(list_1))
    print('  '.join(list_2))
    print('  '.join(list_3))
    print('  '.join(list_4))
    print('  '.join(list_5))


def print_player_board(row_num, col_num):
    """
    Takes two integers and updates the values in each player_list variable with
    an '@' symbol to represent a ships location.
    """
    if row_num == 0:
        player_list_1[col_num] = "@"
    elif row_num == 1:
        player_list_2[col_num] = "@"
    elif row_num == 2:
        player_list_3[col_num] = "@"
    elif row_num == 3:
        player_list_4[col_num] = "@"
    elif row_num == 4:
        player_list_5[col_num] = "@"


def slice_list_for_player_board(list):
    """
    Recieves a list and slices it into 5 lists that will
    be used to by another fucntion to print player board.
    """
    slice_1 = list[0:5]
    player_list_1.extend(slice_1)
    slice_2 = list[5:10]
    player_list_2.extend(slice_2)
    slice_3 = list[10:15]
    player_list_3.extend(slice_3)
    slice_4 = list[15:20]
    player_list_4.extend(slice_4)
    slice_5 = list[20:25]
    player_list_5.extend(slice_5)


def gen_cpu_ship_locations():
    """
    Samples 4 values randomly from a list. These coordinate values are then
    added to another list and repesent the ship locations targeted by
    the player.
    """
    four_ship_locations = random.sample(computer_ship_locations, 4)
    new_cpu_ship_locations.extend(four_ship_locations)


def gen_and_print_player_ships():
    """
    Radomly generates player ship locations and prints to CPUs board.
    This function generates two random integers, one for row and
    one for column. The row and column number are then appended to
    the "storage" list.
    The function then checks if the 'computer_storage'
    list contains the 'storage' list.
    If the computer_storage list does not already contain the 'storage' value,
    the 'storage' list is appended.
    When the storage list has been appended to the computer_storage list
    4 times, the function then prints the player lists which have been updated
    using the values from the computer storage list.
    """
    while True:
        random_row_num = random.randint(0, 4)
        random_col_num = random.randint(0, 4)
        storage = []
        storage.append(random_row_num)
        storage.append(random_col_num)
        if storage not in player_ship_locations:
            player_ship_locations.append(storage)
            print_player_board(random_row_num, random_col_num)
        if len(player_ship_locations) > 3:
            break
    print(f"\n{' '.join(player_name)}'s Board:")
    print('  '.join(player_list_1))
    print('  '.join(player_list_2))
    print('  '.join(player_list_3))
    print('  '.join(player_list_4))
    print('  '.join(player_list_5))


def game_logic():
    """
    This function is a loop that accepts player and cpu guesses, then validates
    the player guesses are not text or outside range 0 - 4. The guesses are
    then printed. Then the scores are printed and incremented by 1 if
    any player hits a ship. Then the player is prompted to enter values to
    either continue playing the game or quit. If the player continues, the
    loop begins again and will end only if the player quits or the score
    increments to 4.
    """
    while True:
        player_input_validator()
        cpu_input_validator()
        print("-" * 70)
        print("At the end of this round, your score is ", end="")
        print(f"{PLAYER_SCORE}, the Computer's score is {CPU_SCORE}")
        print("-" * 70)
        result = quit_game_or_continue_input()
        quit_or_continue(result)
        if PLAYER_SCORE > 3 and CPU_SCORE < 4:
            print("-" * 70)
            print("You have sank all of the CPU's ships! ", end="")
            print("Congratulations, you win!")
            print("-" * 70)
            break
        elif CPU_SCORE > 3 and PLAYER_SCORE < 4:
            print("-" * 70)
            print("The CPU has sank all of your ships!", end="")
            print("Commiserations, you lose!")
            print("-" * 70)
            break
        elif PLAYER_SCORE == 4 and CPU_SCORE == 4:
            print("-" * 70)
            print("Tie game! All ships have been wiped out lol")
            print("-" * 70)
            break


def end():
    """
    Prints 'game over' when game is over.
    """
    print("\nGame Over...\n")


def user_input_col():
    """
    Prompts user to enter column number. If the value entered is not
    between 0 - 5, a message will be printed asking user to try again.
    If the valueError is raised, a message will be printed requesting
    the user enter a number.
    """
    while True:
        try:
            y = int(input("\nChoose a column number:\n"))
            if y in range(0, 5):
                break
            elif y not in range(0, 5):
                print(f"\n{y} is not between 0 and 4.,", end="")
                print('Please choose a column number between 0 and 4.')
        except ValueError:
            print('\nThe value you entered is not a number.', end="")
            print("Please enter a number.")
    return y


def user_input_row():
    """
    Prompts user to enter row number. If the value entered is not
    between 0 - 5, a message will be printed asking user to try again.
    If the valueError is raised, a message will be printed requesting
    the user enter a number.
    """
    while True:
        try:
            x = int(input("\nChoose a row number:\n"))
            if x in range(0, 5):
                break
            elif x not in range(0, 5):
                print(f'\n{x} is not between 0 and 4.', end="")
                print(" Please choose a number between 0 and 4.\n")
        except ValueError:
            print('\nThe value you entered is not a number.', end="")
            print(" Please enter a number.\n")

    return x


def quit_game_or_continue_input():
    """
    prompts user to continue or quit programme. The input is forced
    to lowercase.
    """
    result = input("Enter any key to continue or n to quit game.       ")
    return result.lower()


def quit_or_continue(value):
    """
    Recieves one value, 'n' to quite programe or any other key to
    continue playing the game.
    """

    if value == "n":
        print("\nYou chose to quit. Exiting game...")
        exit()
    else:
        print('\nYou chose to continue...\n')


def play_new_game_or_quit(value):
    """
    Recieves one value, 'n' to quite programe or any other key to
    play a new game.
    """
    if value == "n":
        print("\nYou chose to quit. Exiting game...")
        return True
        exit()
    else:
        print('\nStarting new game...\n')


def print_user_input(col, row):
    """
    Prints message informing the user of the coloumn and row numbers chosen.
    """
    print(f'\nYou have chosen row {row} and column {col}.')


def print_cpu_input(row, col):
    """
    Prints message informing the user of the coloumn and row numbers chosen.
    """
    print(f'\nComputer has chosen row {row} and column {col}')


def compare_input(input_value):
    """
    Prints message if the players guess values match randomly generated
    values that represent CPU players ship locations.
    """
    global PLAYER_SCORE
    ship_locations = new_cpu_ship_locations
    if input_value in ship_locations:
        print("You scored a direct hit!!!")
        PLAYER_SCORE += 1
    else:
        print("You missed...")


def compare_cpu_input(input_value):
    """
    Prints message if the CPU players guess values match randomly generated
    values that represent players ship locations.
    """
    global CPU_SCORE
    if input_value in player_ship_locations:
        print("The Computer scored a direct hit!!!")
        CPU_SCORE += 1
    else:
        print("The Computer missed...")


def player_input_validator():
    """
    Creates a list using the validated row and column numbers chosen by the
    user. The list is then compared with the player_guesses list and appended
    to the player_guessses list if not already present, and the cpu player's
    board will be updated and printed. If the players chosen coordintes are in
    the list, a message is printed informing the user of this and prompts the
    user to try again.
    """
    while True:
        row_num = user_input_row()
        col_num = user_input_col()
        player_guess = []
        player_guess.append(row_num)
        player_guess.append(col_num)
        if player_guess not in player_guesses:
            store_player_guesses(row_num, col_num)
            print_updated_computer_board(row_num, col_num, player_guess)
            print_user_input(col_num, row_num)
            compare_input(player_guess)
            break
        else:
            print("\nYou have already chosen these coordinates,", end="")
            print(" please try again...")


def cpu_input_validator():
    """
    Creates a list using the row and column numbers chosen by the
    cpu. The list is then compared with the cpu_guesses list and appended
    to the cpu_guessses list if not already present and the players board
    will be updated and printed. If the cpu player's guess is already present,
    the loop will begin again.
    """
    while True:
        cpu_row_num = rand_row_num()
        cpu_col_num = rand_col_num()
        cpu_guess = []
        cpu_guess.append(cpu_row_num)
        cpu_guess.append(cpu_col_num)
        if cpu_guess not in cpu_guesses:
            store_cpu_guesses(cpu_row_num, cpu_col_num)
            print_updated_player_board(cpu_row_num, cpu_col_num, cpu_guess)
            print_cpu_input(cpu_row_num, cpu_col_num)
            compare_cpu_input(cpu_guess)
            break


def store_cpu_guesses(row_num, col_num):
    """
    Appends two integers (CPU players row and column guess) to cpu_guesses
    variable as a list.
    """
    cpu_guesses.append([row_num, col_num])


def store_player_guesses(row_num, col_num):
    """
    Appends two integers (players row and column guess) to player_guesses
    variable as a list.
    """
    player_guesses.append([row_num, col_num])


def print_updated_computer_board(row_num, col_num, ship_location):
    """
    Receives a row number, column number and a list of lists that contain
    coordinates that represent the cpu ships locations.
    The players coordinate guesses are compared with the cpu's ship
    coordinates.
    If the two sets of coordinates match, the ship_hit function is called.
    If the two sets of coordinates do not match, the ship_missed function
    is called.
    """
    ship_location = [row_num, col_num]
    ship_locations = new_cpu_ship_locations
    row_num = ship_location[0]
    col_num = ship_location[1]
    if ship_location in ship_locations:
        ship_hit(row_num, col_num)
    else:
        ship_missed(row_num, col_num)


def print_updated_player_board(row_num, col_num, ship_locations):
    """
    Receives a row number, column number and a list of lists that contain
    coordinates that represent the players ships locations.
    The cpu coordinate guesses are compared with the players ship coordinates.
    If the two sets of coordinates match, the cpu_hit_ship function is called.
    If the two sets of coordinates do not match, the cpu_missed_ship function
    is called.
    """

    ship_location = [row_num, col_num]
    ship_locations = player_ship_locations
    row_num = ship_location[0]
    col_num = ship_location[1]
    if ship_location in ship_locations:
        cpu_hit_ship(row_num, col_num)
    else:
        cpu_missed_ship(row_num, col_num)


def ship_missed(row_num, col_num):
    """
    Receives a row and column number which are used to update lists
    used to print cpu player's board when the player 'misses' any of
    the cpus ships.
    """
    if row_num == 0:
        list_1[col_num] = "x"
    elif row_num == 1:
        list_2[col_num] = "x"
    elif row_num == 2:
        list_3[col_num] = "x"
    elif row_num == 3:
        list_4[col_num] = "x"
    elif row_num == 4:
        list_5[col_num] = "x"
    print("\nCPU Player Board:")
    print('  '.join(list_1))
    print('  '.join(list_2))
    print('  '.join(list_3))
    print('  '.join(list_4))
    print('  '.join(list_5))


def ship_hit(row_num, col_num):
    """
    Receives a row and column number which are used to update lists
    used to print CPU player's board when the player 'hits' any of the
    CPU's ships.
    """
    if row_num == 0:
        list_1[col_num] = "*"
    elif row_num == 1:
        list_2[col_num] = "*"
    elif row_num == 2:
        list_3[col_num] = "*"
    elif row_num == 3:
        list_4[col_num] = "*"
    elif row_num == 4:
        list_5[col_num] = "*"
    print("\nCPU Player Board:")
    print('  '.join(list_1))
    print('  '.join(list_2))
    print('  '.join(list_3))
    print('  '.join(list_4))
    print('  '.join(list_5))


def cpu_missed_ship(row_num, col_num):
    """
    Receives a row and column number which are used to update lists
    used to print player's board when the cpu 'misses' any of the players
    ships.
    """
    if row_num == 0:
        player_list_1[col_num] = "x"
    elif row_num == 1:
        player_list_2[col_num] = "x"
    elif row_num == 2:
        player_list_3[col_num] = "x"
    elif row_num == 3:
        player_list_4[col_num] = "x"
    elif row_num == 4:
        player_list_5[col_num] = "x"
    print(f"\n{' '.join(player_name)}'s Board:")
    print('  '.join(player_list_1))
    print('  '.join(player_list_2))
    print('  '.join(player_list_3))
    print('  '.join(player_list_4))
    print('  '.join(player_list_5))


def cpu_hit_ship(row_num, col_num):
    """
    Receives a row and column number which are used to update lists
    used to print player's board when the cpu 'hits' any of the players ships.
    """
    if row_num == 0:
        player_list_1[col_num] = "*"
    elif row_num == 1:
        player_list_2[col_num] = "*"
    elif row_num == 2:
        player_list_3[col_num] = "*"
    elif row_num == 3:
        player_list_4[col_num] = "*"
    elif row_num == 4:
        player_list_5[col_num] = "*"
    print(f"\n{' '.join(player_name)}'s Board:")
    print('  '.join(player_list_1))
    print('  '.join(player_list_2))
    print('  '.join(player_list_3))
    print('  '.join(player_list_4))
    print('  '.join(player_list_5))


def rand_row_num():
    """
    Randomly generates an interger between 0 and 4 and returns this value.
    This value will determine the CPU's row number guess.
    """
    random_row_num = random.randint(0, 4)
    return random_row_num


def rand_col_num():
    """
    Randomly generates an interger between 0 and 4 and returns this value.
    This value will determine the CPU's column number guess.
    """
    random_col_num = random.randint(0, 4)
    return random_col_num


def main():
    """
    Runs all functions
    """
    while True:
        reset_game_values()
        intro_msg()
        add_name()
        generate_list()
        print_cpus_board(generate_list())
        slice_list_for_player_board(generate_list())
        gen_cpu_ship_locations()
        gen_and_print_player_ships()
        game_logic()
        end()
        result = quit_game_or_continue_input()
        if play_new_game_or_quit(result):
            exit()


main()