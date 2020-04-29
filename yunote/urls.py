from django.urls import path
from .views import *

app_name = 'yunote'

urlpatterns = (
    path('note/', create_view, name='create_view'),
    path('list/', list_view, name='list_view'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user_logout/', logoutUser, name='user'),
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('<id>/delete/', delete_view, name='delete'),
    path('<id>/update/', update_view, name='update'),
)
