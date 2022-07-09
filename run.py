import random

computer_board_list = [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "@", "@", "@", "@"]

list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []


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


def compare_input(input_value, rand_value):
    """
    Prints message if user input values match randomly generated values
    """
    if input_value == rand_value:
        print("Direct hit!!!")
        return True
    else:
        print("You missed")
        return False


def player_guess_compare(rand_value):
    """
    Gets input values from user and appends to list before comparing with
    randomly generated values.If the value of the lists match, a message is
    printed to inform the user a ship has been hit, the loop breaks and the
    game ends. If the values dont match, a message is printed informing the
     user that they 'missed' and the loop continues.
    """
    while True:
        row_num = user_input_row()
        col_num = user_input_col()
        player_guess = []
        player_guess.append(row_num)
        player_guess.append(col_num)
        print_user_input(col_num, row_num)
        print_updated_computer_board(row_num, col_num)
        memory(row_num, col_num)
        if compare_input(player_guess, rand_value):
            break


def end():
    """
    Prints game over when game is over.
    """
    print("game over")


def print_updated_computer_board(row_num, col_num):
    """
    Prints updated computer player board.
    """

    row_number = row_num
    col_number = col_num

    if row_number == 0:
        list_1[col_number] = "x"
    elif row_number == 1:
        list_2[col_number] = "x"
    elif row_number == 2:
        list_3[col_number] = "x"
    elif row_number == 3:
        list_4[col_number] = "x"
    elif row_number == 4:
        list_5[col_number] = "x"
    print('  '.join(list_1))
    print('  '.join(list_2))
    print('  '.join(list_3))
    print('  '.join(list_4))
    print('  '.join(list_5))


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
    print('  '.join(list_1))
    print('  '.join(list_2))
    print('  '.join(list_3))
    print('  '.join(list_4))
    print('  '.join(list_5))


# def shuffled_list(returned_list, row_num, col_num):
#     """
#     Slices shuffled list before printing 5 lists to represent
#     computers player board.
#     """
    
#     slice_1 = returned_list[0:5]
#     list_1.extend(slice_1)
#     slice_2 = returned_list[5:10]
#     list_2.extend(slice_2)
#     slice_3 = returned_list[10:15]
#     list_3.extend(slice_3)
#     slice_4 = returned_list[15:20]
#     list_4.extend(slice_4)
#     slice_5 = returned_list[20:25]
#     list_5.extend(slice_5)

#     row_number = row_num
#     col_number = col_num

#     if row_number == 0:
#         list_1[col_number] = "x"
#     elif row_number == 1:
#         list_2[col_number] = "x"
#     elif row_number == 2:
#         list_3[col_number] = "x"
#     elif row_number == 3:
#         list_4[col_number] = "x"
#     elif row_number == 4:
#         list_5[col_number] = "x"
#     print('  '.join(list_1))
#     print('  '.join(list_2))
#     print('  '.join(list_3))
#     print('  '.join(list_4))
#     print('  '.join(list_5))


storage = []


def memory(row_num, col_num):
    storage.append([row_num, col_num])
    print(f'The latest value for memory test is {storage}')


def main():
    """
    Runs all functions
    """
    intro_msg()
    returned_list = list_shuffler()
    shuffled_list(returned_list)
    rand_value = random_ship_gen()
    player_guess_compare(rand_value)
    end()


main()