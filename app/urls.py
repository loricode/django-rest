from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from empresa.views import PersonaViewSet

router = DefaultRouter()
router.register(r'personas', PersonaViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]