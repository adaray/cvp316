def data_input():
    tx_recipient = input('Enter recipient name: ')
    tx_amount = float(input('Enter amount: '))
    return tx_recipient, tx_amount


    recipient, amount = data_input()
    transaction = {'recipient': recipient, 'amount': amount}
    print(transaction)


def guess_number():
    import random
    num = random.randint(1,10)
    num_list = [num]
    guess = int(input('Guess the number: '))
    while guess != num:
        if guess > num:
            print('Number is large.')
        else:
            print('Number is small.')
        guess = int(input('Try again: '))
        num_list.append(num)
    print('Well done!, you guessed right, answer = ',num)
    print('Listed numbers: ', num_list)


def investment():
    inv = 5000
    inv_d = inv * 2
    rate = 1.1
    n = 0
    while inv < inv_d:
        inv = inv*rate
        n+=1
        print('After year', n,'the investment is', inv)
    #print(n)
    #print(inv)

#investment()

def prime_check():
    # n = int(input('Check number: '))
    # for i in range(2,n):
    #     if (i != n) & (n % i == 0):
    #         print(n, 'is not a prime number')
    #     else:
    #         print(n, 'is prime number')
    import math        
    a = int(input('Check the number: '))
    n = 3
    #x = a % n == 0

    while (x!=0) & (n<=math.sqrt(a)):
        n = n+2
        
        if a % n == 0:
            print('not prime')
    if x != 0:
        print('prime') 


prime_check()

