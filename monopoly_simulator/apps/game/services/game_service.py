from apps.game.entities.player import Player
from apps.game.entities.property import Property
from apps.game.enums.player_type import PlayerType
import random
import copy


class GameService:
    def __init__(self):
        self.__create_properties()
        self.max_turns = 1000

    def __roll_dice(self) -> int:
        dice = random.randint(1, 6)
        return dice

    def __set_players(self):
        self.players = [Player(player_type=ptype) for ptype in PlayerType]
        random.shuffle(self.players)
        self.original_players = copy.deepcopy(self.players)

    def __create_properties(self):
        rents = [
            35,
            75,
            50,
            85,
            25,
            40,
            60,
            90,
            45,
            100,
            20,
            55,
            30,
            65,
            95,
            80,
            70,
            85,
            40,
            50,
        ]
        self.properties = [Property(rent=rent, value=rent * 3) for rent in rents]

    def simulate_game(self) -> Player:
        self.__set_players()
        current_turn = 0
        for _ in range(self.max_turns):
            player = self.players[current_turn]
            self.__play_round(player)
            current_turn = (current_turn + 1) % len(self.players)

            if len(self.players) == 1:
                break

        return self.__get_winner()

    def __get_winner(self) -> Player:
        return max(self.players, key=lambda p: p.balance)

    def __play_round(self, player: Player):
        dice = self.__roll_dice()
        position = player.move(dice, len(self.properties))

        property = self.properties[position]

        if property.owner:
            self.__pay_rent(player, property)
        else:
            player.buy_property(property)

    def __pay_rent(self, player: Player, property: Property):
        if property.owner != player:
            owner = property.owner
            if player.balance <= property.rent:
                money_to_receive = player.balance
                self.__remove_player_from_the_game(player)
            else:
                money_to_receive = property.rent

            player.balance -= money_to_receive
            owner.balance += money_to_receive

    def __remove_player_from_the_game(self, player: Player):
        self.players.remove(player)
        for property in player.properties:
            property.owner = None
