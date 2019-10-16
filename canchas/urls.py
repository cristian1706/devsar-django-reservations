from rest_framework import routers

from .views import CanchaViewSet, ReservaViewSet, UsuarioViewSet

router = routers.DefaultRouter()
router.register('canchas', CanchaViewSet)
router.register('reservas', ReservaViewSet)
router.register('usuarios', UsuarioViewSet)

urlpatterns = router.urls