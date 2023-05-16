from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from API import views


router = DefaultRouter()
router.register(r'Products', views.ProductListView)
router.register(r'PriceDisplay', views.PriceDisplayListView)
router.register(r'ProductChange', views.ProductChangeView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)