import hashlib

users = {
    "admin": hashlib.sha256("1234".encode()).hexdigest(),
    "kasir": hashlib.sha256("5678".encode()).hexdigest()
}

def login(username: str, password: str) -> bool:
    # secure coding: autentikasi menggunakan hashing
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return users.get(username) == hashed
