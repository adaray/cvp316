# Initialising our empty blockchain list
MINING_REWARD = 10

genesis_block = {
    'previous_hash':'', 
    'index': 0,
    'transactions': []
}

blockchain = [genesis_block]
open_transaction = []
owner = 'Ahmed'
participants = {'Ahmed'}

def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender']==participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transaction if tx['sender']== participant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient']==participant] for block in blockchain]
    amount_recieved = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_recieved += tx[0]
    return amount_recieved - amount_sent

def last_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']
  
def get_tx_value():
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Enter transaction value: '))
    return tx_recipient, tx_amount

def get_user_choice():
    return input('\nEnter your choice: ')

def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain

    Arguments:
        :sender: The sender of the coins
        :recipient: The recipient of the coins
        :amount:  The amount of coins sent (default = 1.0)
    """
    transaction = { 'sender': sender,
                    'recipient': recipient,
                    'amount': amount}
    
    if verify_transaction(transaction):
        open_transaction.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])
 
def mine_block():
    last_block = blockchain[-1]
    hashed_block =  hash_block(last_block)
    #print(hashed_block)
    reward_transaction = {
        'sender':'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transaction = open_transaction[:]
    copied_transaction.append(reward_transaction)
    block = { 'previous_hash':hashed_block, 
            'index': len(blockchain),
            'transactions': copied_transaction}
    blockchain.append(block)
    return True


def print_blockchain():
    for block in blockchain:
            print('\nOutputting Block\n')
            print(block)
    else:
        print('--' * 15)


def verify_chain():
    """ Verify current blockchain returns True or False """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False
    return True

while True:
    print('\nPlease make a choice: \n')
    print('1: Add a new transaction block: ')
    print('2: Mine a new block')
    print('3: Display current block chain blocks: ')
    print('4: Output participants')
    print('h: Manipulate the chain')
    print('q: To quit the program: ')

    user_choice = get_user_choice()

    if user_choice == '1':
        recipient, amount = get_tx_value()
        if add_transaction(recipient, amount=amount):
            print('Transaction succeeded')
        else:
            print('Transaction failed!')
        print(open_transaction)
    
    elif user_choice == '2':
        if mine_block():
            open_transaction = []
    
    elif user_choice == '3':
        print_blockchain()
    
    elif user_choice == '4':
        print(participants)

    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0]={ 'previous_hash':'', 
                            'index': 0,
                            'transactions': [{'sender':'chris',
                            'recipient':'Max', 'amount':100.0}]}
            
    elif user_choice == 'q':
        break 
    else:
        print("\nWrong selection, please try again\n")

    if not verify_chain():
        print('\nInvalid blockchain')
        break
    print('Balance of {}: {:6.2f}'.format('Ahmed', get_balance('Ahmed')))

print('\nDone!')