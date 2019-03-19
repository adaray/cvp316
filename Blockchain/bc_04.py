genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}

blockchain = [genesis_block]
open_transactions = []
owner = 'Ahmed'

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient':recipient,
        'amount': amount
    }
    open_transactions.append(transaction)
 
def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def mine_block():
    hashed_block = hash_block(blockchain[-1])
    print(hashed_block)

    block = { 
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)

def get_transaction_value():
    tx_recipient = input('Enter recipient: ')
    tx_amount = float(input('Enter transaction value: '))
    return tx_recipient, tx_amount

def print_blockchain():
    
    for block in blockchain:
        print('\nOutputting Blocks')
        print(block)
    else:
        print('_'*25)



def verify_chain():
    for index, block in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] == hash_block(blockchain[index-1]):
            return False
        return True

while True:
    print('\nMenu Choice \n')
    print('1: Add transaction')
    print('2: Mine a block')
    print('3: Display the blockchain')
    print('h: Manimpulate the chain')
    print('q: Quit the program\n')
    choice = input('Make a choice: ')
    if choice == '1':
        tx_recipient, tx_amount = get_transaction_value()
        add_transaction(tx_recipient, amount=tx_amount)
        #print(open_transactions)
    elif choice == '2':
        mine_block()
    elif choice == '3':
        print_blockchain()
    elif choice == 'h':
        blockchain[0] = {
            'previous_hash': '',
            'index': 0,
            'transactions': [{'sender':'Max', 'recipient':'Mo', 'amount': 100.0}]
        }
    elif choice == 'q':
        break
    else:
        print('Invalid selection, please try again')
    if verify_chain():
        print_blockchain()
        print('Invalid Transaction')
        break

print('\nDone!')

