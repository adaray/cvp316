import hashlib as hl
from wallet import Wallet

class Verification:


    @staticmethod
    def valid_proof(transaction, last_hash, proof):
        guess_hash = hl.sha256((str([tx.ordered_dict() for tx in transaction]) + str(last_hash) + str(proof)).encode()).hexdigest()
        return guess_hash[0:2] == '00'

    @classmethod
    def verify_chain(cls, blockchain, hash_block):
        for index, block in enumerate(blockchain):
            if index >= 1:
                if block.previous_hash == hash_block(blockchain[index-1]):
                    return False
                if not cls.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                    print('Proof of work is invalid!')
                    return False
                return True

    @staticmethod
    def verify_transaction(transaction, get_balance, check_funds=True):
        if check_funds:
            sender_balance = get_balance()
            return sender_balance >= transaction.amount and Wallet.verify_transaction(transaction)
        else:
            return Wallet.verify_transaction(transaction)
    @classmethod
    def verify_transactions(cls, open_transactions, get_balance):
        return all([cls.verify_transaction(tx, get_balance, False) for tx in open_transactions])





