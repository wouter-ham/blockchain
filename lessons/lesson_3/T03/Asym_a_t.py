from Asym import *

# Read the encrypted message from "message_test.enc"
# Read Keys file from "sample_test.keys"   File format is similar to the previous tutorial
# Check and print who is the receiver of this message

if __name__ == '__main__':
    loaded_keys = load_keys('T03/samples_test.keys')

    with open('T03/message_test.enc', 'rb') as file:
        content = file.read()
        for item in loaded_keys:
            key_name, prv_key, pbc_key = item
            decrypted = decrypt(b'{content}', prv_key)

            if decrypted:
                print('sender: ' + key_name)
                print(decrypted)
            else:
                print('wrong')
