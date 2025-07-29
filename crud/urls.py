from django.urls import path
from . import views

urlpatterns = [
     path('', views.manage, name='manage'),  # هذا يعالج الرابط الرئيسي /

    path('manage/<int:pk>/', views.manage, name='manage_edit'),  # لتعديل عنصر موجود
]
