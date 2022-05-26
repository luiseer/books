from .views import BookItemViewSet, BookItemLendViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("book-item", BookItemViewSet)
router.register("book-item-lend", BookItemLendViewSet)


urlpatterns = router.urls