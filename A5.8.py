print("A5.8 ---- Password")
CORRECT_PASSWORD = "TAHERIM"

password = ""

while password != CORRECT_PASSWORD:
    password = input("Enter password: ")

    if password != CORRECT_PASSWORD:
        print("Incorrect password. Please try again.\n")

print("Access granted!")
