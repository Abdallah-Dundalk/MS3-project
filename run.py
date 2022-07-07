def intro_msg():
    """
    Prints welcome message to terminal
    """
    print("Lets Play Battle Ship\n")


def user_input_col():
    """
    Prompts user to enter column number
    """
    user_col_num = input("Enter column number\n")
    return user_col_num


def user_input_row():
    """
    Prompts user to enter row number
    """
    user_row_num = input("Enter row number\n")
    return user_row_num


def print_user_input(col, row):
    """
    Prints message informing the user of the coloumn and row numbers chosen
    """
    print(f'You have chosen col {col} and row {row}')


def main():
    """
    Runs all functions
    """
    intro_msg()
    col_num = user_input_col()
    row_num = user_input_row()
    print_user_input(col_num, row_num)


main()
