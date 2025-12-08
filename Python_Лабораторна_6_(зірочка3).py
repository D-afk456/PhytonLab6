import random

secret = random.randint(1, 100)
attempts = 7

print("Я загадав число від 1 до 100. У тебе 7 спроб!")

while attempts > 0:
    guess = input(f"Введи число (залишилось спроб: {attempts}): ")

    # Перевірка коректності вводу
    if not guess.isdigit():
        print("Введи ціле число!")
        continue

    guess = int(guess)

    if guess == secret:
        print("Вітаю! Ти вгадав число! 🎉")
        break
    elif guess < secret:
        print("Більше!")
    else:
        print("Менше!")

    attempts -= 1

if attempts == 0:
    print(f"Спроби закінчилися. Ти програв! Загадане число було: {secret}")
