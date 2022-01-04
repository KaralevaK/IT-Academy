# from django.conf.urls import url
from django.urls import path, include
from .views import complete_todo, index, create, delete_todo, search, edit, update, deadline_today, register

urlpatterns = [
    path('', index, name='home'),
    path('create', create, name='create'),
    path('delete_todo/<int:id>/', delete_todo),
    path('search', search, name='search'),
    path('complete_todo/<int:id>/', complete_todo),
    path('edit/<int:id>/', edit, name='edit'),
    path('update/<int:id>/', update, name='update'),
    path('deadline', deadline_today, name='deadline'),
    path('register/', register, name = 'register'),
]

urlpatterns += [ path('accounts/', include('django.contrib.auth.urls')),]