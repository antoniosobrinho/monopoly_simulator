from rest_framework import viewsets
from rest_framework.response import Response

from apps.game.services.game_service import GameService
from apps.game.api.serializers.game_result_serializer import GameResultSerializer
from apps.game.dtos.game_result_dto import GameResultDTO


class GameViewSet(viewsets.ViewSet):
    def list(self, request):
        game_service = GameService()
        winner = game_service.simulate_game()
        players = game_service.original_players

        game_result = GameResultDTO(winner=winner, players=players)
        serializer = GameResultSerializer(instance=game_result)

        return Response(serializer.data)
