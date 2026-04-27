from collections import deque

def palindrome(text: str) -> bool:
    d = deque()

    for char in text.lower():
        if char != " ":
            d.append(char)

    # порівнюємо символи з обох кінців черги
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True

while True:
    text = input("Write text (or 'exit'): >>> ")
    
    if text.lower() == "exit":
        break

    print(palindrome(text))