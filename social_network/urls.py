from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.urls import path, include

from .views import UserViewSet, PostViewSet, IndexView, register


router = DefaultRouter()
router2 = DefaultRouter()
router.register(r'users', UserViewSet)
router2.register(r'posts', PostViewSet)

urlpatterns = [
	path('', IndexView.as_view(), name="index"),
	path('register/', register, name="register"),
	path('login/', LoginView.as_view(template_name='login.html'), name="login"),
	path('logout/', LogoutView.as_view(next_page='/social_network'), name="logout"),
	path('token/', views.obtain_auth_token, name='auth'),
	path('api/', include(router.urls)),
	path('api/', include(router2.urls)),
]
