from cryptography.fernet import Fernet
import hashlib
import hmac

def hash_password(password, secret_key):
    return hmac.new(secret_key.encode(), password.encode(), hashlib.sha256).hexdigest()

def verify_password(password, hashed_password, secret_key):
    return hmac.compare_digest(hash_password(password, secret_key), hashed_password)

def generate_key():
    """AES 암호화를 위한 키 생성"""
    return Fernet.generate_key()

def encrypt_message(key, message):
    """메시지 암호화"""
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(key, encrypted_message):
    """암호화된 메시지 복호화"""
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()
