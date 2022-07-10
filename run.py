import random

computer_board_list = [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
player_board_list = [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
computer_ship_locations = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
new_cpu_ship_locations = []
player_ship_locations = []
list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []

player_list_1 = [".", ".", ".", ".", "."]
player_list_2 = [".", ".", ".", ".", "."]
player_list_3 = [".", ".", ".", ".", "."]
player_list_4 = [".", ".", ".", ".", "."]
player_list_5 = [".", ".", ".", ".", "."]

PLAYER_SCORE = 0
NUM_OF_SHIPS = 0
CPU_SCORE = 0


player_guesses = []

# need to chnage this variable name to player_board_generator
computer_guesses = []

cpu_guesses = []

def list_shuffler():
    random.shuffle(computer_board_list)
    return computer_board_list


def intro_msg():
    """
    Prints welcome message to terminal
    """
    print("Lets Play Battle Ship\n")


def user_input_col():
    """
    Prompts user to enter column number and returns an integer
    """
    user_col_num = int(input("Enter column number\n"))
    return user_col_num


def user_input_row():
    """
    Prompts user to enter row number and returns an integer.
    """
    user_row_num = int(input("Enter row number\n"))
    return user_row_num


def print_user_input(col, row):
    """
    Prints message informing the user of the coloumn and row numbers chosen.
    """
    print(f'You have chosen row {row} and column {col}')


def random_ship_gen():
    """
    Generates two random integers and appends to empty list.
    """
    random_integer_1 = random.randint(0, 4)
    random_integer_2 = random.randint(0, 4)
    random_integer_list = []
    random_integer_list.append(random_integer_1)
    random_integer_list.append(random_integer_2)
    print(random_integer_list)
    return random_integer_list


def cpu_ship_values():
    four_ship_locations = random.sample(computer_ship_locations, 4)
    new_cpu_ship_locations.extend(four_ship_locations)


def compare_input(input_value):
    """
    Prints message if user input values match randomly generated values
    """
    global PLAYER_SCORE
    ship_locations = new_cpu_ship_locations
    if input_value in ship_locations:
        print("You scored a direct hit!!!")
        PLAYER_SCORE += 1
        # return True
    else:
        print("You missed")
        # return False


def compare_cpu_input(input_value):
    """
    Prints message if user input values match randomly generated values
    """
    global CPU_SCORE
    ship_locations = computer_guesses
    if input_value in computer_guesses:
        print("The Computer Scored A Direct hit!!!")
        CPU_SCORE += 1
        # return True
    else:
        print("The Computer missed")
        # return False

def player_guess_compare():
    """
    Gets input values from user and appends to list before comparing with
    randomly generated values.If the value of the lists match, a message is
    printed to inform the user a ship has been hit, the loop breaks and the
    game ends. If the values dont match, a message is printed informing the
     user that they 'missed' and the loop continues.
    """
    while True:
        print(f'\nYour score is {PLAYER_SCORE}, the Computers score is {CPU_SCORE}')
        row_num = user_input_row()
        col_num = user_input_col()
        player_guess = []
        player_guess.append(row_num)
        player_guess.append(col_num)
# this is where the computer makes a guess
        cpu_row_num = rand_row_num()
        cpu_col_num = rand_col_num()
        cpu_guess = []
        cpu_guess.append(cpu_row_num)
        cpu_guess.append(cpu_col_num)
        
        print_user_input(col_num, row_num)
        print_cpu_input(cpu_row_num, cpu_col_num)
        print_updated_computer_board(row_num, col_num)
        print_updated_player_board(cpu_row_num, cpu_col_num)
        store_cpu_guesses(cpu_row_num, cpu_col_num)
        store_player_guesses(row_num, col_num)
        compare_input(player_guess)
        compare_cpu_input(cpu_guess)
        if PLAYER_SCORE > 3 or CPU_SCORE > 3:
            print(PLAYER_SCORE)
            break





def store_cpu_guesses(row_num, col_num):
    cpu_guesses.append([row_num, col_num])


def store_player_guesses(row_num, col_num):
    player_guesses.append([row_num, col_num])


def end():
    """
    Prints game over when game is over.
    """
    print("game over")


def print_updated_computer_board(row_num, col_num):
    """
    Prints updated computer player board.
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
    print("\nCPU Player Board")
    print('  '.join(list_1))
    print('  '.join(list_2))
    print('  '.join(list_3))
    print('  '.join(list_4))
    print('  '.join(list_5))


def print_updated_player_board(row_num, col_num):
    """
    Prints updated computer player board.
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
    print("\nPlayer Board")
    print('  '.join(player_list_1))
    print('  '.join(player_list_2))
    print('  '.join(player_list_3))
    print('  '.join(player_list_4))
    print('  '.join(player_list_5))

def shuffled_list(returned_list):
    """
    Slices shuffled list before printing 5 lists to represent
    computers player board.
    """

    slice_1 = returned_list[0:5]
    list_1.extend(slice_1)
    slice_2 = returned_list[5:10]
    list_2.extend(slice_2)
    slice_3 = returned_list[10:15]
    list_3.extend(slice_3)
    slice_4 = returned_list[15:20]
    list_4.extend(slice_4)
    slice_5 = returned_list[20:25]
    list_5.extend(slice_5)
    print("\nCPU Player board")
    print('  '.join(list_1))
    print('  '.join(list_2))
    print('  '.join(list_3))
    print('  '.join(list_4))
    print('  '.join(list_5))







# player board code below this line...........................................

# def player_ship_values():
#     four_ship_locations = random.sample(computer_ship_locations, 4)
#     player_ship_locations.extend(four_ship_locations)
#     print(player_ship_locations)
#     row_num_1 = player_ship_locations[0][0]
#     row_num_2 = player_ship_locations[1][0]
#     row_num_3 = player_ship_locations[2][0]
#     row_num_4 = player_ship_locations[3][0]
#     col_num_1 = player_ship_locations[0][1]
#     col_num_2 = player_ship_locations[1][1]
#     col_num_3 = player_ship_locations[2][1]
#     col_num_4 = player_ship_locations[3][1]


def rand_row_and_col():
    while True:
        random_row_num = random.randint(0, 4)
        random_col_num = random.randint(0, 4)
        storage = []
        storage.append(random_row_num)
        storage.append(random_col_num)
        
        if storage not in computer_guesses:
            computer_guesses.append(storage)
            print_player_board(random_row_num, random_col_num)
        if len(computer_guesses) > 3:
            break
    print("\nPlayer Board")
    print('  '.join(player_list_1))
    print('  '.join(player_list_2))
    print('  '.join(player_list_3))
    print('  '.join(player_list_4))
    print('  '.join(player_list_5))
            

def rand_row_num():
    random_row_num = random.randint(0, 4)
    return random_row_num


def rand_col_num():
    random_col_num = random.randint(0, 4)
    return random_col_num


def print_player_board(row_num, col_num):
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


def print_cpu_input(col, row):
    """
    Prints message informing the user of the coloumn and row numbers chosen.
    """
    print(f'Computer has chosen row {row} and column {col}')


def print_updated_player_board(row_num, col_num):
    """
    Prints updated computer player board.
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
    print("Player Board")
    print('  '.join(player_list_1))
    print('  '.join(player_list_2))
    print('  '.join(player_list_3))
    print('  '.join(player_list_4))
    print('  '.join(player_list_5))





# def Gen_player_ship_location():
#     row_num = random.randint(0, 4)
#     col_num = random.randint(0, 4)
#     ship_location = []
#     ship_location.append(row_num)
#     ship_location.append(col_num)
#     print(f'{ship_location} is the ship location randomly generated')
#     return ship_location


# def check_ship_values(ship_location):
#     global NUM_OF_SHIPS
#     ship_locations = player_ship_locations
#     for x in range(4):
#         if ship_location not in ship_locations:
#             print(f'this is passed from the other function {ship_location}')
#             ship_locations.append(ship_location)
#             print(f' this is updated ship list after{ship_locations}')
#             NUM_OF_SHIPS = NUM_OF_SHIPS+1
#             print(NUM_OF_SHIPS)
#         else:
#             continue



def main():
    """
    Runs all functions
    """
    intro_msg()
    cpu_ship_values()
    returned_list = list_shuffler()
    shuffled_list(returned_list)
    rand_row_and_col()
    player_guess_compare()
    end()
    

main()