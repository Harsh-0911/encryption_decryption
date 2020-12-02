def display_menu():
    '''
    Displays menu to the user.
    '''
    print('-' * 30)
    print(('-' * 13) + 'Menu' + ('-' * 13))
    print('1. Encrypt a message')
    print('2. Decrypt a message')
    print('-' * 30)
    print()


def get_message():
    '''
    Take input from the user.

    :return: message of the user as string.
    '''
    print('-' * 30)
    message = input('Enter Your Message: ')

    return message
