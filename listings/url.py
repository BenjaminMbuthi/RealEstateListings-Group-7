from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, LocationViewSet, PropertyViewSet, BuyerViewSet, ListingViewSet

router = DefaultRouter()
router.register(r'agents', AgentViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'buyers', BuyerViewSet)
router.register(r'listings', ListingViewSet)

urlpatterns = router.urls
