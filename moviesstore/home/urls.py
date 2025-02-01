from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home.index'),
    path('<int:id>/', views.show, name='home.show'),
    path('<int:id>/review/create/', views.create_review,
        name='home.create_review'),
    path('<int:id>/review/<int:review_id>/edit/',
        views.edit_review, name='home.edit_review'),
]