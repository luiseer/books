from .views import BookItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("book-item", BookItemViewSet)
urlpatterns = router.urls

