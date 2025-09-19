import random
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
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def getting_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
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


def printing_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def getting_deposit():
    while True:
        Deposit = input("Enter the Deposit amount: ")
        if Deposit.isdigit():
            Deposit = int(Deposit)
            if Deposit > 0:
                break
            else:
                print("Amount must be greater then zero ! ")
                continue
        else:
            continue
    return Deposit


def getting_lines():
    while True:
        bet_lines = input("How many lines you want: ")
        if bet_lines.isdigit():
            bet_lines = int(bet_lines)
            if bet_lines != 0 and bet_lines <= 3:
                break
            else:
                print("lines are limitted from 1 to 3")
                continue
        else:
            print("write a valid number!")
            continue
    return bet_lines


def get_bet():
    while True:
        Bet_ammount = input("Enter the bet amount for each line: ")
        if Bet_ammount.isdigit():
            Bet_ammount = int(Bet_ammount)
            if MIN_BET <= Bet_ammount <= MAX_BET:
                break
            else:
                print(f"Bet boundries are from {MIN_BET} to {MAX_BET}")
                continue
        else:
            print("Enter a valid number!")
            continue
    return Bet_ammount


def spin(balance):
    lines = getting_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting {bet} on {lines} lines. Total bet is equal to: {total_bet}")

    slots = getting_slot_machine_spin(ROWS, COLS, symbol_count)
    printing_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = getting_deposit()
    while True:
        print(f"Your current balance is: {balance}")
        answer = input("Press enter to play and q for quit.")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You are left with ${balance}")


main()