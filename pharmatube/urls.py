from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products.views import *

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'labs', LaboratoryViewSet)
router.register(r'users', UserViewSet)
router.register(r'sells', SellViewSet)
router.register(r'racks', RackViewSet)
router.register(r'storings', StoringViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
