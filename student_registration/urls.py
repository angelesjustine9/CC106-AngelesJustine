from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('home.urls')),

    # Login URL
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),

    # Logout URL
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # Registration app URL
    path('registration/', include('registration.urls')),
]