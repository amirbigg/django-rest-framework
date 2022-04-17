from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token
from rest_framework import routers


app_name = 'accounts'
urlpatterns = [
	path('register/', views.UserRegister.as_view()),
	path('api-token-auth/', auth_token.obtain_auth_token),
]

router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls
