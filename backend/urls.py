from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from api.views import StudentRecordViewSet

router = DefaultRouter()
router.register(r'student-records', StudentRecordViewSet, basename='student-records')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('api/', include(router.urls)),
]