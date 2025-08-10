from django.urls import path
from . import views

app_name = 'telegram_bot_task'

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    # API Info endpoint
    path('api-info/', views.gif_api_info, name='api_info'),
    
    # GIF generation endpoint
    path('generate-gif/', views.GenerateGifView.as_view(), name='generate_gif'),
]
