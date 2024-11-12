import hashlib

# Function to hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Example stored logins with hashed passwords
stored_logins = {
    "user1@example.com": hash_password("password123"),
    "user2@example.com": hash_password("securepassword"),
    "user3@example.com": hash_password("letmein")
}

# Login function
def login(email, password_to_check):
    # Hash the password provided for checking
    password_hash = hash_password(password_to_check)
    
    # Check if the email exists in stored_logins and the hashes match
    return stored_logins.get(email) == password_hash

# Example usage
print(login("user1@example.com", "password123"))  # Should return True
print(login("user2@example.com", "wrongpassword"))  # Should return False
