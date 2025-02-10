import hashlib
import os
import sqlite3

# 🚨 Hardcoded credentials (Semgrep will flag this)
password = "SuperSecret123"

# 🚨 Weak hashing algorithm (MD5 is insecure)
hashed_password = hashlib.md5(password.encode()).hexdigest()
print(f"Hashed Password (MD5): {hashed_password}")

# 🚨 SQL Injection Vulnerability
user_input = "105 OR 1=1"
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
query = "SELECT * FROM users WHERE user_id = " + user_input  # 🚨 This is unsafe!
cursor.execute(query)
result = cursor.fetchall()
print("SQL Injection Risk! Fetched Results:", result)

# 🚨 Unvalidated user input
user_age = input("Enter your age: ")  # ⚠️ Not validated
print(f"User entered age: {user_age}")

# 🚨 Hardcoded API Key
API_KEY = "12345-ABCDE-SECRET-KEY"
print(f"Using API Key: {API_KEY}")
