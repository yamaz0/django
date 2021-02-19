from users.views import UserViewSet
from users.views import GroupViewSet
from users.views import ChangePasswordView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'password', ChangePasswordView, basename='userPassword')