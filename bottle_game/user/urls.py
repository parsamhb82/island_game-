from django.urls import path
from .views import Login, Refresh, RegisterPlayerView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('refresh/', Refresh.as_view(), name='refresh'),
    path('register/', RegisterPlayerView.as_view(), name='register')
]

