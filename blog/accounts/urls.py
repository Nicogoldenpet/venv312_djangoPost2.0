from django.urls import path
from .views import SignUpView

urlpatterns = [ #Definiendo las urls para registrarse y cerrar sesión
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logged_out/', SignUpView.as_view(), name='logged_out'),
]