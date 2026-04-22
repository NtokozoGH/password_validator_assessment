"""
PYTHON CHALLENGE: THE MULTI-STAGE SECURITY CHECK
-----------------------------------------------
Your task is to write the logic for three separate security modules. 
Follow the requirements for each question carefully.
"""

# --- QUESTION 1: THE BASIC GATEKEEPER ---
# 1. Ask for a password input.
# 2. If it's shorter than 6 characters, print "Too Short".
# 3. If it's "123456" OR "password", print "Too Simple".
# 4. Otherwise, print "Validating...".

password = input("Question 1 - Set a password: ")
# Write logic here:
if len(password) <6:
    print("Too Short")
elif password == "123456" or password == "password":
    print("Too Simple")
else: print("Validating")


# --- QUESTION 2: THE MULTI-FACTOR SIMULATION ---
# Ask for two inputs: a password AND a "PIN" (as an integer).
# 1. If the password is "Admin" AND the PIN is 9999, print "Superuser Access".
# 2. If the password is "Admin" but the PIN is wrong, print "Invalid PIN".
# 3. If the password is wrong, print "Access Denied".

pwd = input("Question 2 - Enter Password: ")
pin = int(input("Question 2 - Enter 4-digit PIN: "))
# Write logic here:
if pwd == "Admin" and pin == 9999:
    print("Superuser Access")
elif pwd == "Admin" and pin != 9999:
    print("Invalid PIN")
else: 
    pwd != "Admin"
    print("Access Denied")

# --- QUESTION 3: THE COMPLEXITY BOSS ---
# Rules for a "Master Password":
# 1. It must be between 10 and 20 characters long.
# 2. It must NOT contain the word "login" (in any case).
# 3. It must start with the character "!" or "@".
#
# If all 3 rules are met, print "Password Robust!".
# If any rule is failed, print "Weakness Detected".

master_pwd = input("Question 3 - Create Master Password: ")
# Write logic here:
length_ok = len(master_pwd) >=10 and len(master_pwd) <=20
log_out="login" not in master_pwd 
begin_with= master_pwd[0]== "!" or master_pwd[0]== "@"
if length_ok and log_out and begin_with :
    print("Password Robust!")
else:
    print("weakness Detected")


