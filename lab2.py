import random

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
print("Weapons: ", weapons)

try:
    weaponRoll = random.randint(1, 6)
    print(f"Weapon roll: {weaponRoll}")

    hero_weapon = weapons[weaponRoll - 1]
    print(f"Your hero's weapon: {hero_weapon}")

    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    if hero_weapon != "Fist":
        print("Thank goodness you didn't roll the Fist..")

except IndexError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
