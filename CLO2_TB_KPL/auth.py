users = {
    "admin": "1234",
    "kasir": "5678"
}

def login(username: str, password: str) -> bool:
    return users.get(username) == password
