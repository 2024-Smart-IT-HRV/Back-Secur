from cryptography.fernet import Fernet

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
