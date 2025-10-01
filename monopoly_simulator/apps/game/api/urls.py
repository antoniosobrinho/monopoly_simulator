from rest_framework import routers

from apps.game.api.viewsets.game_viewset import GameViewSet

router = routers.SimpleRouter()
router.register(r"simular", GameViewSet, basename="simular")

urlpatterns = router.urls
