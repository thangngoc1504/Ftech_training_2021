from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:question_id>', views.detailView, name='detail'),
    path('list/', views.list_question, name='list'),
    path('<int:question_id>', views.vote, name='vote'),
]