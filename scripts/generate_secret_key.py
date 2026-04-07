import secrets

def generate_secret_key():
    return secrets.token_urlsafe(32)

if __name__ == "__main__":
    key = generate_secret_key()
    print("🔐 Generated SECRET_KEY:\n")
    print(f"SECRET_KEY={key}")