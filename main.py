def displayMenu():
    print('\nMenu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


def encode(password):
    res = ''
    for letter in password:
        res += str(int(letter)+3)
    print('Your password has been encoded and stored!')
    return res


def decode(_password):
    pass


def main():
    password = ''
    choice = -1

    while True:
        displayMenu()
        choice = int(input('Please enter an option: '))

        if choice == 1:
            password = input('Please enter your password to encode: ')
            password = encode(password)

        if choice == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}')

        if choice == 3:
            break

if __name__ == '__main__':
    main()