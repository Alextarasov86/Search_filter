from django.urls import path
from .views import AuthView, VarifyView

urlpatterns = [
    path('auth/', AuthView.as_view()),
    path('varify/', VarifyView.as_view()),

]