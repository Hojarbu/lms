from django.urls import path

from lms import settings
from django.conf.urls.static import static

from main import views

app_name = "main"

urlpatterns = [
    path('', views.index, name='home'),
    path('users/', views.user_list, name='users'),
    path('user/create/', views.CreateCustomUserView.as_view(), name='create_user'),
    path('user/<int:pk>/update/', views.UpdateCustomUserView.as_view(), name='update_user')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
