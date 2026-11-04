from random import randint


class Fighter:
    """This class represents a generic fighter character."""

    def __init__(self, name, health, defense, power, damage):
        """Initialize the fighter with the given attributes."""
        self.name = name
        self.health = health
        self.defense = defense
        self.power = power
        self.damage = damage


    def alive(self):
        """Determine if the fighter is alive."""

        return self.health > 0


    def attack(self, opponent):
        """Have the fighter attack an opponent."""

        roll = randint(1, 20)
        if roll + self.power - opponent.defense > 12:
            print(f"{self.name} hits {opponent.name} for {self.damage} points")
            opponent.wound(self.damage)
            if not opponent.alive():
                print(f"{self.name} won!")
        elif roll + self.power - opponent.defense > 13:
            print(f"{self.name} hits {opponent.name} for {self.damage * 2} points with a super attack")
            opponent.wound(self.damage * 2)
            if not opponent.alive():
                print(f"{self.name} won!")
        else:
            print(f"{self.name} missed.")


    def wound(self, amount):
        """Apply damage to the fighter."""

        self.health -= amount
        if not self.alive():
            print(f"{self.name} died.")


    def print_status(self):
        """Print the current status of the fighter."""
        print(f"{self.name} has {self.health} health.")


class Wizard:

    def __init__(self, name, health, defense, power, damage):
        """Initialize the fighter with the given attributes."""
        self.name = name
        self.health = health
        self.defense = defense
        self.power = power
        self.damage = damage


    def alive(self):
        """Determine if the fighter is alive."""

        return self.health > 0


    def attack(self, opponent):
        """Have the fighter attack an opponent."""

        roll = randint(1, 20)
        if 12 < roll + self.power - opponent.defense < 15:
            print(f"{self.name} hits {opponent.name} for {self.damage} points")
            opponent.wound(self.damage)
            if not opponent.alive():
                print(f"{self.name} won!")
        elif roll + self.power - opponent.defense > 13:
            print(f"{self.name} hits {opponent.name} for {self.damage * 2} points with a super attack")
            opponent.wound(self.damage * 2)
            if not opponent.alive():
                print(f"{self.name} won!")
        else:
            print(f"{self.name} missed.")


    def wound(self, amount):
        """Apply damage to the fighter."""

        self.health -= amount
        if not self.alive():
            print(f"{self.name} died.")


    def print_status(self):
        """Print the current status of the fighter."""
        print(f"{self.name} has {self.health} health.")


f1 = Fighter(name="Carter", health=10, defense=4, power=5, damage=3)
f2 = Wizard(name="Cameron", health=11, defense=5, power=4, damage=2)


print(f"{f1.name} vs {f2.name}")
print(f"{f1.name} is a fighter, {f2.name} is a wizard")
round = 1

while f1.alive() and f2.alive():
    print(f"\nRound {round}")
    f1.print_status()
    f2.print_status()
    answer = input(f"Should {f1.name} attack? (Y or N) Or should you heal? (H) ")
    if answer.lower() == "y":
        f1.attack(f2)
    if answer.lower() == "h":
        roll = randint(1, 2)
        if roll == 1:
            f1.health += 1
            print(f"{f1.name} healed 1 point")
        else:
            print("Not able to heal")
    if f2.alive():
        answer = input(f"Should {f2.name} attack? (Y or N) Or should you heal? (H) ")
        if answer.lower() == "y":
            f2.attack(f1)
        if answer.lower() == "h":
            roll = randint(1, 2)
            if roll == 1:
                f2.health += 1
                print(f"{f2.name} healed 1 point")
            else:
                print("Not able to heal")
    round += 1

print("Fight over.")


