import random

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
# Define Variables
numLives = 10  # number of player's lives remaining
mNumLives = 12  # number of monster's lives remaining

diceOptions = [1, 2, 3, 4, 5, 6]

def main():
    try:
        combatStrength = int(input("Enter your combat Strength: "))
        mCombatStrength = int(input("Enter the monster's combat Strength: "))

        input("Roll the dice for your health points (Press enter)")
        healthPoints = random.choice(diceOptions)
        print("You rolled " + str(healthPoints) + " health points")


        print(f"Current Combat Strength is {combatStrength}")
        # for the questions
        input("Roll the dice for your Weapon (Press enter)")

        weaponRoll = random.randint(1, 6)

        if weaponRoll != 1:
            print("Thank goodness you didn't roll the Fist...")
        if weaponRoll <= 2:
            print("You rolled a weak weapon, friend")
        elif weaponRoll <= 4:
            print("Your weapon is meh")
        else:
            print("Nice weapon, friend!")

        combatStrength += weaponRoll
        print(f"New combat strength, including weapon {weapons[weaponRoll - 1]}, is {combatStrength}.")

        #

        input("Roll the dice for the monster's health points (Press enter)")
        mHealthPoints = random.choice(diceOptions)
        print("You rolled " + str(mHealthPoints) + " health points for the monster")

        input("Roll the dice to see if you find a healing potion (Press enter)")
        healingPotion = random.choice([0, 1])
        print("Have you found a healing potion?: " + str(bool(healingPotion)))

        input("Analyze the roll (Press enter)")
        # Equality operators
        print("--- You are matched in strength: " + str(combatStrength == mCombatStrength))

        # Relational operators
        print("--- You have a strong player: " + str((combatStrength + healthPoints) >= 15))

        # and keyword
        print("--- Remember to take a healing potion!: " + str(healingPotion == 1 and healthPoints <= 6))

        # not keyword
        print("--- Phew, you have a healing potion: " + str(
            not (  # monster will NOT kill hero in one blow
                    healthPoints < mCombatStrength  # monster will kill hero in one blow
            )
            and
            healingPotion == 1  # hero has a healing potion
        ))

        # or keyword
        print("--- Things are getting dangerous: " + str(healingPotion == 0 or healthPoints == 1))

        # in keyword
        print("--- Is it possible to roll 0 in the dice?: " + str(0 in diceOptions))

        # --- Expanded if statement
        if healthPoints >= 5:
            print("--- Your health is ok")
        elif healingPotion == 1:
            healingPotion = 0
            healthPoints = 6
            print("--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
        else:
            print("--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")

        # --- Nested if statement
        print("You meet the monster. FIGHT!!")
        input("You strike first (Press enter)")
        while healthPoints > 0 and mHealthPoints > 0:
            print("Your weapon (" + str(combatStrength) + ") ---> Monster (" + str(mHealthPoints) + ")")
            if combatStrength >= mHealthPoints:
                mHealthPoints = 0
                print("You've killed the monster")
            else:
                mHealthPoints -= combatStrength

                print("You've reduced the monster's health to: " + str(mHealthPoints))

                print("The monster strikes!!!")
                print("Monster's Claw (" + str(mCombatStrength) + ") ---> You (" + str(healthPoints) + ")")
                if mCombatStrength >= healthPoints:
                    healthPoints = 0
                    print("You're dead")
                else:
                    healthPoints -= mCombatStrength
                    print("The monster has reduced your health to: " + str(healthPoints))

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()