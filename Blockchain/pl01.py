from functools import reduce
import hashlib as hl
import json
from collections import OrderedDict

MINING_REWARD = 10

genesis_block = {
                    'previous_hash': '',
                    'index': 0,
                    'transactions': [],
                    'proof': 100
                }

blockchain = [genesis_block]
open_transactions = []
owner = 'Ahmed'
 
participants = set([])


def hash_block(block):
    #return '-'.join([str(block[key]) for key in block])
    return hl.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

def valid_proof(transaction, last_hash, proof):
    guess_hash = hl.sha256((str(transaction) + str(last_hash) + str(proof)).encode()).hexdigest()
    print(guess_hash)
    return guess_hash[0:2] == '00'

def proof_of_work():
    last_hash = hash_block(blockchain[-1])
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof+=1
    return proof

def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender']== participant]
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
    
    return amount_received - amount_sent

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']

def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])

def add_transactions(recipient, sender=owner, amount=1.0):
    # transactions = {'sender': sender,
    #                'recipient': recipient,
    #                'amount': amount}
    transactions = OrderedDict([('sender', sender),('recipient', recipient), ('amount', amount)])
    if verify_transaction(transactions):
        open_transactions.append(transactions)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False

def mine_block():
    hashed_block = hash_block(blockchain[-1])
    #print(hashed_block)
    proof = proof_of_work()
    # reward_transaction = {'sender': 'MINING',
    #                     'recipient': owner,
    #                     'amount': MINING_REWARD}
    reward_transaction = OrderedDict([('sender', 'MINING'),
                        ('recipient', owner),
                        ('amount', MINING_REWARD)])
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {'previous_hash': hashed_block,
            'index': len(blockchain),
            'transactions': copied_transactions,
            'proof': proof}
    blockchain.append(block)
    return True

def verify_chain():
    for index, block in enumerate(blockchain):
        if index >= 1:
            if hash_block(blockchain[index-1]) == block['previous_hash']:
                return False
            if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
                print('Proof of work is invalid!')
                return False
            return True

def print_blockchain():
    for block in blockchain:
        print('\n')
        print(block)
   
def input_data():
    recipient = input('Enter recipient: ')
    amount = float(input('Enter transaction value: '))
    return recipient, amount

while True:
    print('\nMain menu\n')
    print('1: Add transaction')
    print('2: Mine a block')
    print('3: Display blocks')
    print('4: Show participants')
    print('5: Check transaction validity')
    print('h: Manipulate block')
    print('q: Quit the program\n')
    choice = input('Make a choice: ')
    if choice == '1':
        tx_recipient, tx_amount = input_data()
        if add_transactions(tx_recipient, amount=tx_amount):
            print('Transaction succeeded!')
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif choice == '2':
        if mine_block():
            open_transactions = []
    elif choice == '3':
        print_blockchain()
    elif choice == '4':
        print(participants)
    elif choice == '5':
        if verify_transactions():
            print('All transaction are valid')
        else:
            print('There are invalid transactions')
    elif choice == 'h':
        blockchain[0] = {
                        'previous_hash': '',
                        'index': 0,
                        'transactions': [{'sender':'Nur', 'recipient':'Mo', 'amount': 155.0}]
                        }
    elif choice == 'q':
        break
    else:
        print('Wrong selection, try again')
    if verify_chain():
        print_blockchain()
        print('\nInvalid Blockchain')
        break
    print('Balance: {:6.2f}'.format(get_balance('Ahmed')))

