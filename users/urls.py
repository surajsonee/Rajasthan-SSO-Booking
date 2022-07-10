from django.urls import path, include
from .views import login #logout, profile, 

urlpatterns=[
    # path('profile', profile, name='profile'),
    # path('logout$', logout, name='logout'),
    path('login', login, name='login'),
]