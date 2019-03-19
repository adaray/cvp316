from uuid import uuid4
from bc import Blockchain
from verification import Verification
from wallet import Wallet

class Node:
    def __init__(self):
        #self.wallet.public_key = str(uuid4())
        #self.wallet.public_key = 'Ahmed'
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)

    def print_blockchain(self):
        for block in self.blockchain.get_blockchain():
            print('\n')
            print(block)
    
    def input_data(self):
        recipient = input('Enter recipient: ')
        amount = float(input('Enter transaction value: '))
        return recipient, amount

    def listen_for_input(self):    
        while True:
            print('\nMain menu\n')
            print('1: Add transaction')
            print('2: Mine a block')
            print('3: Display blocks')
            print('4: Check transaction validity')
            print('5: Create a wallet')
            print('6: Load wallet')
            print('7: Save keys')
            print('q: Quit the program\n')

            choice = input('Make a choice: ')
            if choice == '1':
                tx_recipient, tx_amount = self.input_data()
                signature = self.wallet.sign_transaction(self.wallet.public_key, tx_recipient, tx_amount)
                if self.blockchain.add_transactions(tx_recipient,self.wallet.public_key, signature, amount=tx_amount):
                    print('Transaction succeeded!')
                else:
                    print('Transaction failed!')
                print(self.blockchain.get_open_transactions())
            elif choice == '2':
                if not self.blockchain.mine_block():
                    print('Mining failed, no wallet?')
            elif choice == '3':
                self.print_blockchain()
            elif choice == '4':
                if Verification.verify_transactions(self.blockchain.open_transactions, self.blockchain.get_balance):
                    print('All transaction are valid')
                else:
                    print('There are invalid transactions')
            elif choice == '5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif choice == '6':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif choice == '7':
                self.wallet.save_keys()
            elif choice == 'q':
                break
            else:
                print('Wrong selection, try again')
            if Verification.verify_chain(self.blockchain.get_blockchain(), self.blockchain.hash_block):
                self.print_blockchain()
                print('\nInvalid Blockchain')
                break
            print('Balance of {}: {:6.2f}'.format(self.wallet.public_key, self.blockchain.get_balance()))


node = Node()
node.listen_for_input()

