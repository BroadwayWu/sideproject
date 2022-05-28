from django.urls import path
from . import views

app_name='home'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('storymap/', views.storymap, name='storymap'),
    path('checkname/<str:name>', views.checkname, name='checkname'),
    path('survey/', views.survey, name='survey'),
    path('userpattern/', views.userpattern, name='userpattern'),
    path('api-create/', views.api_create, name='api-create'),
    path('api-info/', views.api_info, name='api-info'),
    path('api-update/', views.api_update, name='api-update'),
    path('api-login/', views.api_login, name='api-login'),
    path('api-gender/', views.api_gender, name='api-gender'),
    path('api-career/', views.api_career, name='api-career'),
]