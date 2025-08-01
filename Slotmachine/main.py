import random


MAX_LINES = 3 # in capital as constant value
MAX_BET = 100
MIN_BET = 1

ROWS = 3 
COLS = 3 

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
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
        else: # we can do a for else
            winnings += values[symbol] * bet # this bet is for a single line not all of them
            winning_lines.append(lines + 1) 
    return winnings, winning_lines
    
    
def get_slot_machine_spin(rows, cols, symbol):
    all_symbols = []
    for symbol, symbol_count in symbol.items(): # helps to get every value in a dictionary 
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # putting a : copies every element in a list
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns    


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ") # end basically ends spaces
            else:
                print(column[row], end="")
        print() # this brings a new line 
                
    
def deposit(): # user amount to be inputted
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): # is digit tells if the value inputted is a whole number
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Amount must be greater than 0.")
        else:
            print('Please enter a number.')
    return amount

def get_number_of_lines():
    while True:
        lines = input('Enter the number of lines to bet on (1-' + str(MAX_LINES)+ ')?')
        if lines.isdigit(): 
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print("Enter a valid number of lines.")
        else:
            print('Please enter a number.')
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each lines? $")
        if amount.isdigit(): 
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else: 
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print('Please enter a number.')
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have the enough balance to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines}. Total Bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines  = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winnings_lines)
    return winnings - total_bet



def main():
    balance = deposit()
    while True:
        print(f"Current Balance is ${balance}.")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")


main()