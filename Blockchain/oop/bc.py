from functools import reduce
import hashlib as hl
import json


#Created classes
from block import Block
from transaction import Transaction
from verification import Verification
from wallet import Wallet

MINING_REWARD = 10

class Blockchain:
    def __init__(self, hosting_node_id):
        genesis_block = Block(0, '', [], 100, 0)
        self.__blockchain = [genesis_block]
        self.__open_transactions = []
        self.load_data()
        self.hosting_node = hosting_node_id

    def get_blockchain(self):
        return self.__blockchain[:]
    def get_open_transactions(self):
        return self.__open_transactions[:]

    def load_data(self):
        try:
            with open('blockchain.txt', 'r') as f:
                file_content = f.readlines()
            
                blockchain = json.loads(file_content[0][:-1])
                updated_blockchain = []
                for  block in blockchain:
                    converted_tx = [Transaction(tx['sender'], tx['recipient'], tx['signature'], tx['amount']) for tx in block['transactions']] 
                    updated_block = Block(block['index'], block['previous_hash'], converted_tx, block['proof'])
                    updated_blockchain.append(updated_block)
                
                self.__blockchain = updated_blockchain
                
                open_transactions = json.loads(file_content[1])
                updated_transactions = []
                [updated_transactions.append(Transaction(tx['sender'], tx['recipient'], tx['signature'], tx['amount'])) for tx in open_transactions]
                self.__open_transactions = updated_transactions
        except (IOError, IndexError):
            pass
        finally:
            print('Cleanup')

    
    def save_data(self):
        try:
            with open('blockchain.txt', 'w') as f:
                savable_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash,[tx.__dict__ for tx in block_el.transactions ],block_el.proof, block_el.timestamp) for block_el in self.__blockchain]]
                f.write(json.dumps(savable_chain))
                f.write('\n')
                savable_tx = [tx.__dict__ for tx in self.__open_transactions]
                f.write(json.dumps(savable_tx))
        except IOError:
            print('Saving failed!')


    def proof_of_work(self):
        last_hash = self.hash_block(self.__blockchain[-1])
        proof = 0

        while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
            proof+=1
        return proof

    def hash_block(self, block):
        #return '-'.join([str(block[key]) for key in block])
        hashable_block = block.__dict__.copy()
        hashable_block['transactions'] = [tx.ordered_dict() for tx in hashable_block['transactions']]
        return hl.sha256(json.dumps(hashable_block['transactions'], sort_keys=True).encode()).hexdigest()

    def get_balance(self):
        participant = self.hosting_node
        tx_sender = [[tx.amount for tx in block.transactions if tx.sender == participant] for block in self.__blockchain]
        open_tx_sender = [tx.amount for tx in self.__open_transactions if tx.sender == participant]
        tx_sender.append(open_tx_sender)
        amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
        
        tx_recipient = [[tx.amount for tx in block.transactions if tx.recipient == participant] for block in self.__blockchain]
        amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
        
        return amount_received - amount_sent

    def add_transactions(self, recipient, sender, signature, amount=1.0):
        # transactions = {'sender': sender,
        #                'recipient': recipient,
        #                'amount': amount}
        if self.hosting_node == None:
            return False
        transactions = Transaction(sender, recipient, signature, amount)
        if Verification.verify_transaction(transactions, self.get_balance):
            self.__open_transactions.append(transactions)
            self.save_data()
            return True
        return False

    def mine_block(self):
        if self.hosting_node == None:
            return False
        hashed_block = self.hash_block(self.__blockchain[-1])
        #print(hashed_block)
        proof = self.proof_of_work()
        # reward_transaction = {'sender': 'MINING',
        #                     'recipient': owner,
        #                     'amount': MINING_REWARD}
        reward_transaction = Transaction('MINING', self.hosting_node, '', MINING_REWARD)
    
        copied_transactions = self.__open_transactions[:]
        for tx in copied_transactions:
            if not Wallet.verify_transaction(tx):
                return False        
        copied_transactions.append(reward_transaction)
        block = Block(len(self.__blockchain), hashed_block, copied_transactions, proof)


        self.__blockchain.append(block)
        self.__open_transactions = []
        self.save_data()
        return True



