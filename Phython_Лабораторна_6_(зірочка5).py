# Лабораторна робота №6

# ★ Завдання 5. RPG Битва

import random

hero_hp = 100
monster_hp = 100
round_number = 1

print("🔥 БІЙ РОЗПОЧАТО!")
print("Герой vs Монстр\n")

while hero_hp > 0 and monster_hp > 0:
    print(f"--- Раунд {round_number} ---")

    # Хід героя
    hero_damage = random.randint(5, 20)
    monster_hp -= hero_damage
    if monster_hp < 0:
        monster_hp = 0
    print(f"Герой ударив на {hero_damage} урону. У монстра лишилось {monster_hp} HP")

    if monster_hp == 0:
        break

    # Хід монстра
    monster_damage = random.randint(5, 20)
    hero_hp -= monster_damage
    if hero_hp < 0:
        hero_hp = 0
    print(f"Монстр ударив на {monster_damage} урону. У героя лишилось {hero_hp} HP\n")

    round_number += 1

# Результат бою
if hero_hp > 0:
    print("🏆 Переміг Герой!")
else:
    print("💀 Переміг Монстр!")
