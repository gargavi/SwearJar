from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('user/<int:user_id>', views.user_page, name = "base_user"),
    path('user/<int:user_id>/jar/<int:jar_id>', views.user_page, name = "user_jar"),
    #path('submit/', views.submit, name = "submit"),
]

