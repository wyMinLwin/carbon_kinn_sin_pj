from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserCreateView, UserView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'), 
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('profiles/<int:user_id>/', UserView.as_view(), name='user-profile'),
]
