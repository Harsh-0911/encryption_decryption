import encryption_decryption as ede
import user_input
print('Welcome to the Encryptor - Decryptor v0.0.1')
print('Loading...')


user_input.display_menu()
choice = input(': ')

if choice == '1':
    message = user_input.get_message()
    ede.generate_key()
    encrypted_message = ede.encrypt_message(
        message, ede.load_key())

    print('Encryption Complete..')

    print(f'Encrypted Message: {repr(encrypted_message)[2:-1]}')

elif choice == '2':
    encrypted_message = user_input.get_message()
    decrypted_message = ede.decrypt_message(
        encrypted_message, ede.load_key())

    print('Decryption Complete..')
    print('Decrypted Message: ' + decrypted_message)
else:
    print('Invalid Choice')
    print('Terminatting...')
