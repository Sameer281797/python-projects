print("welcome to the betting game!")


import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A":4,
    "B":4,
    "C":4,
}

symbol_values = {
    "A":4,
    "B":3,
    "C":2,
}

def check_winnings(columns, lines, bet, values):
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
    

def get_slot_machine_spin(rows , cols , symbols):
    all_symbols = []
    for symbol , symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end =" | ")
            else:
                print(column[row],end="")
        print()

def deposite():
    while True:
        amount = input("What would you like to deposite? INR RS:")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 10 :
                break
            else:
                print("your minimum deposite must be INR RS:10 ")
        else:
            print("please enter number")

    return amount

def get_numbers_of_lines():
    while True:
        lines = input(f"Enter the number of line to bet on (1 - {MAX_LINES}) ? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else:
                print("Please enter a valid numbers of line")
        else:
            print("please enter number")

    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on choosen line? INR RS:")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between (RS:{MIN_BET} - RS:{MAX_BET})")
        else:
            print("please enter number")

    return bet

def spin(balance):
    lines = get_numbers_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: INR RS:{balance}")
            main()
        else:
            break

    print(f"You are betting INR RS:{bet} on line number {lines}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won INR RS:{winnings}")
    print(f"You won on line number:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposite()
    while True:
        print(f"Current balance is INR RS:{balance}")
        if balance < 10:
            ans = input("insufficient balance, deposite amount to play more or press q to quit.")
            if ans == "q":
                print("thanks for playing!")
                break
            
            else:
                main()
        else:
            answer = input("Press enter to play (q to quit).")
            if answer == "q":
                break
            balance += spin(balance)

    print(f"You left with INR RS:{balance}")


main()