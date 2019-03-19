blockchain = []

def tx_input():
    return float(input('Enter value: '))

def last_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_transaction(last_transaction, transaction):
    blockchain.append([last_transaction, transaction])
    return blockchain

def print_blocks():
    print('\n Outputting blocks')
    [print(block) for block in blockchain]

def menu():
    return input('Enter choice: ')

while True:
    print('1: Add transaction')
    print('q: Quit the program')
    choice = menu()
    if choice == '1':
        add_transaction(last_value(), tx_input())
    elif choice == 'q':
        break
    print_blocks()     





print_blocks()