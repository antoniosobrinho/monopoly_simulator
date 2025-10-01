from typing import List
from rest_framework import serializers

from apps.game.dtos.game_result_dto import GameResultDTO


class GameResultSerializer(serializers.Serializer):
    vencedor = serializers.SerializerMethodField()
    jogadores = serializers.SerializerMethodField()

    def get_vencedor(self, obj: GameResultDTO) -> str:
        winner = obj.winner
        return winner.player_type.value

    def get_jogadores(self, obj: GameResultDTO) -> List[str]:
        return [p.player_type.value for p in obj.players]
