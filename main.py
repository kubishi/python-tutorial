import random

# Player
player = {
    "Name": "Sir Python",
    "HP": 100,
    "Damage": (10, 25),  # Damage will be a random number between these two
    "Potions": 3  # The player starts with three potions
}

# Enemy
enemy = {
    "Name": "Code Ogre",
    "HP": 150,  # The enemy is stronger now
    "Damage": (10, 20)  # The enemy deals more damage
}

def attack(attacker, defender):
    # Calculate random damage
    damage = random.randint(attacker["Damage"][0], attacker["Damage"][1])
    defender["HP"] -= damage

    print(f"{attacker['Name']} attacks! {defender['Name']} takes {damage} damage.")
    print(f"{defender['Name']}'s HP: {defender['HP']}\n")

def drink_potion(character):
    if character["Potions"] > 0:
        character["HP"] += 50  # Restore 50 HP
        character["Potions"] -= 1  # Use up one potion
        print(f"{character['Name']} drinks a potion and recovers 50 HP.")
        print(f"{character['Name']}'s HP: {character['HP']}\n")
    else:
        print(f"{character['Name']} has no potions left!\n")

while True:
    # Player's turn
    print(f"{player['Name']} HP: {player['HP']}, Potions: {player['Potions']}")
    action = input("Enter 'a' to attack or 'p' to drink a potion: ")
    if action.lower() == 'a':
        attack(player, enemy)
        if enemy["HP"] <= 0:
            print("You have defeated the Code Ogre. Congratulations!")
            break
    elif action.lower() == 'p':
        drink_potion(player)

    # Enemy's turn
    if enemy["HP"] > 0:
        attack(enemy, player)
        if player["HP"] <= 0:
            print("You have been defeated by the Code Ogre. Game Over.")
            break
