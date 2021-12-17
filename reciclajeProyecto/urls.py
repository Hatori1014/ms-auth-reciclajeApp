from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from reciclajeAplicacion import views

urlpatterns = [
    path('iniciarSesion/', TokenObtainPairView.as_view()),
    path('actualizar/', TokenRefreshView.as_view()),
    path('verificaToken/', views.VerificaTokenView.as_view()),
    path('autenticacion/users/', views.AutenticacionListView.as_view(), name="Listar usuarios"),
    path('autenticacion/', views.AutenticacionCreateView.as_view(), name="Creación de usuario"),
    path('autenticacion/<int:pk>/', views.AutenticacionDetailView.as_view(), name="Detalle de Usuario por ID"),
    path('autenticacion/delete/<int:pk>/', views.AutenticacionDeleteView.as_view(), name="Eliminación de usuario por ID"),
    path('autenticacion/update/<int:pk>/', views.AutenticacionUpdateView.as_view(), name="Actualización de usuario por ID"),

]