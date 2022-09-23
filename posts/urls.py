from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet,PostViewset #new

router=SimpleRouter()
router.register("users", UserViewSet,basename="users")
router.register("",PostViewset,basename="posts")
urlpatterns=router.urls