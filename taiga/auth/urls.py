from django.urls import path

from .views import TokenRefreshView, TokenObtainPairView
#from .views import TokenVerifyView

urls = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

