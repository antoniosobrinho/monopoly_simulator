from dataclasses import dataclass
from typing import List
from apps.game.entities.player import Player


@dataclass
class GameResultDTO:
    winner: Player
    players: List[Player]
