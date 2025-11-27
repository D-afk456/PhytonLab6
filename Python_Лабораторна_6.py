# Лабораторна робота №6
# Завдання: Банкомат
import time

CORRECT_PIN = "1234"
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    entered_pin = input(f"Спроба {attempt}. Введіть PIN-код: ")

    if entered_pin == CORRECT_PIN:
        print("Перевірка даних...")
        time.sleep(1) # Чекає 1 секунду
        print("З'єднання з банком...")
        time.sleep(2) # Чекає 2 секунди
        print("ВХІД ДОЗВОЛЕНО! Ласкаво просимо.")
        break
    else:
        if attempt == max_attempts:
            print("Картку заблоковано")
        else:
            print("Невірний PIN-код. Спробуйте ще раз.")
