prime_checker_max_number = 1000 * 1000
prime_lister_max_number = 1000 * 100
msg_tryagain = "Try again!"

def is_prime(n):
    x = 2
    while x < n:
        if n % x == 0:
            return False
        else:
            x = x + 1
    return True

def prime_checker():
    max_number = prime_checker_max_number
    while True:
        print()
        n = input('Please enter a positive number (1 - %s): ' % (max_number))
        if not(n):
            return False
        if n.isdigit():
            n = int(n)
            if n == 0:
                return True
            if n > max_number:
                print(msg_tryagain)
            else:
                if is_prime(n):
                    print(n, ' is Prime.')
                else:
                    print(n, ' is not prime.')
        else:
            print(msg_tryagain)

def prime_lister():
    max_number = prime_lister_max_number
    while True:
        print()
        n = input('Please enter a positive number (1 - %s): ' % (max_number))
        if not(n):
            return False
        if n.isdigit():
            n = int(n)
            if n == 0:
                return True
            if n > max_number:
                print(msg_tryagain)
            else:
                x = 1
                while x <= n:
                    if is_prime(x):
                        print(x)
                    x = x + 1
        else:
            print(msg_tryagain)

while True:
    print()
    print('MENU')
    print('1) Primer Checker')
    print('2) Prime Number lister')
    print('Press ENTER to exit')
    print()
    user_input = input('Please enter your selection: ')
    if user_input:
        if user_input == '1':
            if prime_checker():
                continue
            else:
                break
        if user_input == '2':
            if prime_lister():
                continue
            else:
                break
    else:
        break
    
