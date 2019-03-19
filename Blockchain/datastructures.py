simple_list = [1,2,3,4]
simple_list.extend([5,7,8,9,10])

blockchain = []

def add_tx(tx):
    return blockchain.append(tx)

def print_block():
    if len(blockchain) < 2:
        return None
    return print([blockchain[-2], tx])
    
def hash_block(block):
    return '-'.join([str(block[key]) for key in block]) 
    
while True:
    print('\nMenu Choice\n')
    print('1: Add Transaction')
    print('q: Quit the program')

    choice = input('Menu choice: ')

    if choice == '1':
        tx = float(input('Enter value: '))
        add_tx(tx)
    elif choice == 'q':
        break
    print(blockchain)
    print_block()
    


