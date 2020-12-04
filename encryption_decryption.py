from cryptography.fernet import Fernet


def generate_key():
    '''
    This function generates encryption key and stores it in a file called as 'secret-key.key'.
    '''
    print('Generating Key...')
    key = Fernet.generate_key()
    with open('secret_key.key', 'wb') as f:
        f.write(key)
    print(f'Encryption Key: {repr(key)[2:-1]}')
    print('WARNING: Only recently generated key is stored in the file.')


def load_key():
    '''
    This functions loads the encryption key from the file called as 'secret-key.key'

    :return: encryption key in bytes. 
    '''
    key = open("secret_key.key", "rb").read()
    return key


def encrypt_message(message, key):
    '''
    This fumction encrypts the message using the the key.

    :param message: Message to be encrypted
    :param key: Encryption key
    :return: Encrypted message
    '''
    f = Fernet(key)
    message = message.encode()
    encrypted_message = f.encrypt(message)

    return encrypted_message


def decrypt_message(encrypted_message, decryption_key):
    '''
    This function decrypts the encrypted_message using the decryption_key.

    :param encrypted_message: Encrypted Message (the message should be without prefix [b'] and suffix ['])
    :param decryption_key: key which is generated at the time of encryption
    :return: Decrypted message
    '''
    encrypted_message = bytes(encrypted_message, 'utf-8')
    f = Fernet(decryption_key)
    decrypted_message = f.decrypt(encrypted_message)
    decrypted_message = decrypted_message.decode()

    return decrypted_message
