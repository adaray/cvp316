from collections import OrderedDict
from printable import Printable

class Transaction(Printable):
    def __init__(self, sender, recipient, signature, amount):
        self.recipient = recipient
        self.sender = sender
        self.amount = amount
        self.signature = signature

    def ordered_dict(self):
        return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('amount', self.amount)])


