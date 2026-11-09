import random





class Player:
    def __init__(self, name, coins, health, damage, level, DEFAULT_VALUES):
        self.name = name
        self.coins = coins
        self.health = health
        self.damage = damage
        self.level = level
        self.DEFAULT_VALUES = {
    "health":100,
    "damage":10,
    "level":1,
    "coins":50
}

    def __str__(self):
        return (f"====================\n"
                f"{f'{self.name} ({self.level})':^20}\n"
                f"====================\n"
                f"{'Coins:':<10}{self.coins:>10}\n"
                f"{'Health:':<10}{self.health:>10}\n"
                f"{'Damage:':<10}{self.damage:>10}\n"
                f""
                )


def create_player():
    name = input("Please enter your character's name: ")
    defaults = Player.DEFAULT_VALUES
    health, damage, level, coins = (
        defaults["health"], defaults["damage"], defaults["level"], defaults["coins"]
    )


