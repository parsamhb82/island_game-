from django.urls import path
from .views import SendBottleView, ReadSentBottles, ViewAvailabeBottlesToBuy, BuyBottleView, ViewAbilitiesTobuy, BuyAbilityToReply, BuyAbilityToReadMore, ReplyToBottle
urlpatterns = [
    path("send-bottle/", SendBottleView.as_view()),
    path("read-sent-bottles/", ReadSentBottles.as_view()),
    path("view-available-bottles/", ViewAvailabeBottlesToBuy.as_view()),#check
    path('buy-bottle/', BuyBottleView.as_view()),
    path('view-abilities-tobuy/', ViewAbilitiesTobuy.as_view()),
    path('buy-ability-to-reply/', BuyAbilityToReply.as_view()),
    path('buy-ability-to-read-more/', BuyAbilityToReadMore.as_view()),
    path('reply-to-bottle/', ReplyToBottle.as_view()),


]