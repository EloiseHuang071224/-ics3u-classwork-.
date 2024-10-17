PIN = "12345"
tries = 0

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")
tries += 1

while entry != PIN and tries < 4:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")
    tries += 1

if entry == PIN:
    print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
elif tries >= 4:
    print("\nYOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED.")




PIN = "12345"
tries = 0

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")
tries += 1

while entry != PIN and tries < n:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")
    tries += 1

if entry == PIN:
    print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
elif tries >= n:
    print("\nYOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED.")

