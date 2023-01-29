
from django.contrib import admin
from django.urls import path

from rest_framework import routers

from ts_elektrik.views import FactoryViewSet, Retail_networkViewSet, Sole_traderViewSet

router = routers.SimpleRouter()
router.register('factory', FactoryViewSet)
router.register('retail_network', Retail_networkViewSet)
router.register('sole_trader', Sole_traderViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
