import random


MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count =  {           #How many symbols are allowed to generate
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value =  {           #How much to multiply symbols on 3 matching in a single line
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):            #
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)      #Randomly selects symbols for spin based on how many lines are selected
            current_symbols.remove(value)       #Removes symbols out of the selection pool
            column.append(value)        

        columns.append(column)
            
    return columns




def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()




def deposit():
    while True:
        amount = input("How much would you like to deposit? $ ")
        if amount.isdigit():      #.isdigit ensures the input amount is a number  
            amount = int(amount)        #int(amount) ensures the input amount is a whole number
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount




def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():      #.isdigit ensures the input amount is a number
            lines = int(lines)     #int(lines) ensures the input amount is a whole number 
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines




def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $ ")
        if amount.isdigit():            #.isdigit ensures the input amount is a number
            amount = int(amount)        #int(amount) ensures the input amount is a whole number
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on line:", *winning_lines)
    return winnings - total_bet


def main():                 #Start of game; user input first
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
