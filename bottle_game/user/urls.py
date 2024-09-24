from django.urls import path
from .views import Login, Refresh, RegisterPlayerView, PlayersScoresSheet, FillTheMap

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('refresh/', Refresh.as_view(), name='refresh'),
    path('register/', RegisterPlayerView.as_view(), name='register'),
    path('score_sheet/', PlayersScoresSheet.as_view(), name='score_sheet'),
    path('fill_the_map/', FillTheMap.as_view(), name='fill_the_map'),
]

