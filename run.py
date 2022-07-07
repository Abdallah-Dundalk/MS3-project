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
    print(f'You have chosen column {col} and row {row}')


def compare_input(input_value):
    if input_value == [1, 2]:
        print("Direct hit!!!")
    else:
        print("You missed")


def main():
    """
    Runs all functions
    """
    intro_msg()
    col_num = user_input_col()
    row_num = user_input_row()
    player_guess = []
    player_guess.append(col_num)
    player_guess.append(row_num)
    print_user_input(col_num, row_num)
    compare_input(player_guess)


main()
