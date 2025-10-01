from apps.game.enums.player_type import PlayerType
from apps.game.entities.property import Property
import random


class Player:
    def __init__(self, player_type: PlayerType):
        self.balance = 300
        self.player_type = player_type
        self.position = 0
        self.properties = []

    def move(self, steps: int, board_size: int) -> int:
        old_position = self.position
        self.position = (self.position + steps) % board_size

        if self.position < old_position:
            self.balance += 100

        return self.position

    def buy_property(self, property: Property):
        if self.balance < property.value:
            return

        should_buy = False

        if self.player_type == PlayerType.IMPULSIVE:
            should_buy = True
        elif self.player_type == PlayerType.DEMANDING:
            should_buy = property.rent > 50
        elif self.player_type == PlayerType.CAUTIOUS:
            should_buy = self.balance - property.value >= 80
        elif self.player_type == PlayerType.RANDOM:
            should_buy = random.choice([True, False])

        if should_buy:
            self.balance -= property.value
            property.owner = self
            self.properties.append(property)
