from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('question/', views.view_question,name="view_question"),
    path('choice/', views.view_choice,name="view_choice"),
    path('detail_question/<int:question_id>', views.detai_question,name="detail_question"),
    path('<int:question_id>',views.vote,name="vote"),
]
