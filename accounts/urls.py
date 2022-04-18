from django.urls import path
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'accounts'
urlpatterns = [
	path('register/', views.UserRegister.as_view()),
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls

# {
# 	"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MDM1MTYwMCwiaWF0IjoxNjUwMjY1MjAwLCJqdGkiOiJmZjFhMjBmODdkOWI0Zjk1YWU0MmM0ZGRlMTFmMWFmOCIsInVzZXJfaWQiOjF9.lmt_kWYxwG4c4rgI5DXalUAc1X3o-P2uhu0d33566Xw",
# 	"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUwMjY1NTAwLCJpYXQiOjE2NTAyNjUyMDAsImp0aSI6IjAzZTg5Yzc1OTNiYjRlOTE5NTNhZWUxNjBhOTAxYjc5IiwidXNlcl9pZCI6MX0.kcpkO6hQHShKCGirUbYMSnadKyHVNKS5OIzZuXqurt0"
# }