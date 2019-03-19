blockchain = []

def last_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def get_tx_value():
    return float(input('Enter transaction value: '))

def get_user_choice():
    return input('\nEnter your choice: ')

def add_value(transaction, last_transaction = [1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction])
 


def verify_chain():
    #block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index-1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index +=1
    return is_valid
            

    # for block in blockchain:
    #     if block_index == 0:
    #         block_index+=1
    #         continue
    #     elif block[0] == blockchain[block_index-1]:
    

def print_blockchain():
    for block in blockchain:
            print('\nOutputting Block\n')
            print(block)
    else:
        print('--' * 15)


while True:
    print('\nPlease make a choice: \n')
    print('1: Add a new transaction block: ')
    print('2: Display current block chain blocks: ')
    print('h: Manipulate the chain')
    print('q: To quit the program: ')

    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_tx_value()
        add_value(tx_amount, last_value())
    
    elif user_choice == '2':
        print_blockchain()
    
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[2]=[1.11]
            
    elif user_choice == 'q':
        break 
    else:
        print("\nWrong selection, please try again\n")

    if not verify_chain():
        print('\nInvalid blockchain')
        break
  
print('\nDone!')