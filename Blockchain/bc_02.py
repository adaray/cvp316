blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_transaction(transaction_amount, last_transaction = [1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
    return float(input('Enter transaction value: '))
    
def print_blockchain():
    print('\nOutputting Blocks')
    for block in blockchain:
        print(block)
    else:
        print('_'*25)


def verify_chain():
    for index in range(len(blockchain)):
        if index >= 1:
            if blockchain[index-1] == blockchain[index][0]:
                return False
            return True


while True:
    print('\nMenu Choice \n')
    print('1: Add transaction')
    print('2: Display the blockchain')
    print('h: Manimpuate the chain')
    print('q: Quit the program\n')
    choice = input('Make a choice: ')
    if choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif choice == '2':
        print_blockchain()
    elif choice == 'h':
        blockchain[0] = [2]
    elif choice == 'q':
        break
    else:
        print('Invalid selection, please try again')
    if verify_chain():
        print('Invalid Transaction')
        break

print('\nDone!')

