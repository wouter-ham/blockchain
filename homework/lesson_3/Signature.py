import pickle

from cryptography.exceptions import *
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey


def generate_keys() -> (RSAPrivateKey, RSAPublicKey):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key


def sign(message: str, private_key: RSAPrivateKey) -> bytes | bool:
    try:
        return private_key.sign(
            bytes(message, 'utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    except:
        return False


def verify(message: str, signature: bytes, public_key: RSAPublicKey) -> bool:
    try:
        public_key.verify(
            signature,
            bytes(message, 'utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False


def save_keys(keys_file_name: str, keys: (RSAPrivateKey, RSAPublicKey), pw: str) -> None:
    private_key, public_key = keys

    private: RSAPrivateKey = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(bytes(pw, 'utf-8'))
    )
    public: RSAPublicKey = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    file = open(keys_file_name, "wb")
    pickle.dump((private, public), file)
    file.close()


def load_keys(keys_file_name: str, pw: str) -> (RSAPrivateKey, RSAPublicKey):
    file = open(keys_file_name, "rb")
    pr, pu = pickle.load(file)
    file.close()

    private: RSAPrivateKey = serialization.load_pem_private_key(pr, password=bytes(pw, 'utf-8'))
    public: RSAPublicKey = private.public_key()

    return private, public
