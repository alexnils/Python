# flippblipp-v3.py

def flippblipp(n):
    if n % 3 == 0 and n % 5 == 0:
        return "flipp blipp"
    elif n % 3 == 0:
        return "flipp"
    elif n % 5 == 0:
        return "blipp"
    else:
        return str(n)

# Starta spelet
print("Välkommen till Flipp Blipp!")

# Startvärde
n = 1
print(flippblipp(n))  # Skriver ut första talet

while True:
    n += 1
    user_input = input(f"Vad kommer efter {n-1}? ")

    if user_input == flippblipp(n):
        print(f"Korrekt!")
    else:
        print(f"Fel - rätt svar är \"{flippblipp(n)}\"!")
        print("Game over")
        break
