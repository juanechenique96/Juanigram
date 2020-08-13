# Django
from django.urls import path

# Views
from users import views


urlpatterns = [

    # Management
    path(
        route='login/', 
        view=views.LoginView.as_view(), 
        name='login'
    ),
    path(
        route='logout/', 
        view=views.LogoutView.as_view(), 
        name='logout'
    ),
    path(
        route='signup/', 
        view=views.signup, 
        name='signup'
    ),
    path(
        route='me/profile', 
        view=views.update_profile, 
        name='update'
    ),

    # Posts
    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
]
