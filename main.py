import random
from uuid import uuid4

players = {}

ID = None
CHARACTER = None

class Player:
    DEFAULT_VALUES = {
        "health": 100,
        "damage": 10,
        "level": 1,
        "coins": 50,
    }

    def __init__(self, name, coins, health, damage, level):
        self.name = name
        self.coins = coins
        self.health = health
        self.damage = damage
        self.level = level

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
    """
    Interactively prompts for character creation and initializes a player entry
    using configured default values.

    :raises EOFError: If input cannot be read from the input stream.
    :raises KeyError: If a required default player value is missing.
    """
    if input("Would you like to create a new character? (y/n):").lower() != "y":
        return None
    name = input("Please enter your character's name: ")
    defaults = Player.DEFAULT_VALUES
    player = Player(
        name=name,
        coins=defaults["coins"],
        health=defaults["health"],
        damage=defaults["damage"],
        level=defaults["level"],
    )
    player_id = uuid4()
    players[player_id] = player
    return None


def player_selection():
    """
    Prompt the user to select an available player.

    Displays the current player list, asks the user to choose one by number, and
    repeats the prompt until a valid numeric selection is provided. If no players
    are available, the user is notified and selection is not performed.

    :global players: Collection of available players keyed by player identifier.
    :return: The selected player identifier and player object, or ``None`` when no
        player can be selected.
    :rtype: tuple[Any, Any] | None
    :raises EOFError: If input cannot be read from the input stream.
    :raises KeyboardInterrupt: If the user interrupts input.
    """
    # Checks a character has been created
    if not players:
        input("Please create a character, then try again. Press enter to continue.....")
        return None
    else:
        for i, (player_id, player) in enumerate(players.items()):
            print(f"Player {i+1}: {player.name}")
        print()
        # Validates chosen option
        while True:
            try:
                choice = int(input(f"Which player would you like to choose? (1-{i+1})")) - 1
                if choice > i or choice < 0:
                    input("That is not a valid option. Press enter to pick again.....")
                    continue
                break
            except ValueError:
                input("That is not a valid option. Press enter to pick again.....")
        # Loops through available players and sets variables to the chosen characters variables.
        for i, (player_id, player) in enumerate(players.items()):
            if choice == i:
                return player_id, player
        return None


create_player()

selection = player_selection()
if selection is not None:
    ID, CHARACTER = selection

