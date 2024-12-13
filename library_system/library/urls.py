from rest_framework.routers import DefaultRouter
from .views import BookViewSet, MemberViewSet, LoanViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'members', MemberViewSet, basename='member')
router.register(r'loans', LoanViewSet, basename='loan')

urlpatterns = router.urls
