def flippblipp(n):
    if n % 3 == 0 and n % 5 == 0:
        return "flipp blipp"
    elif n % 3 == 0:
        return "flipp"
    elif n % 5 == 0:
        return "blipp"
    else:
        return str(n)

n = 33  

for i in range(1, n + 1):
    print(flippblipp(i))