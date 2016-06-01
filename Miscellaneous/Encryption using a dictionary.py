letters = {"A": "E", "B": "F", "C": "G", "D": "H",
           "E": "I", "F": "J", "G": "K", "H": "L"}

message = input("Enter you message: ").upper()
encrypted = ""

for letter in message:
    if letter in letters:
        encrypted += letters[letter]
    else:
        encrypted += letter

print(encrypted)


