from tkinter.messagebox import NO
from cryptography.exceptions import *
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import pickle

from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey


def generate_keys() -> (RSAPrivateKey, RSAPublicKey):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key


def encrypt(message: bytes, key: RSAPrivateKey | RSAPublicKey) -> bytes | bool:
    try:
        ciphertext = key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext
    except:
        return False


def decrypt(ciphertext: bytes, key: RSAPrivateKey | RSAPublicKey) -> bytes | bool:
    try:
        plaintext = key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext
    except:
        return False


def save_keys(keys_file_name: str, keys_list: [(str, RSAPrivateKey, RSAPrivateKey)]) -> None:
    keys_serialised_list = []
    for item in keys_list:
        key, private_key, public_key = item

        private: RSAPrivateKey = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        public: RSAPublicKey = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        keys_serialised_list.append((key, private, public))

    file = open(keys_file_name, "wb")
    pickle.dump(keys_serialised_list, file)
    file.close()


def load_keys(keys_file_name: str) -> list:
    file = open(keys_file_name, "rb")
    keys_list_ser = pickle.load(file)
    file.close()

    keys: [(str, RSAPrivateKey, RSAPrivateKey)] = []
    for item in keys_list_ser:
        key, private_key_ser, public_key_ser = item
        private: RSAPrivateKey = serialization.load_pem_private_key(private_key_ser, password=None)
        public: RSAPublicKey = serialization.load_pem_public_key(public_key_ser)

        keys.append((key, private, public))
    return keys
