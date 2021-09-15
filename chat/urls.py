from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('adminpage/', views.adminpage, name="adminpage"),
    path('customer/', views.customer, name="customerPage"),
    path('logout/', views.logoutUser, name="logout"),

    path('new_note', views.new_note, name="new"),
    path('note/<str:pk>', views.note_detail, name='note'),
    path('delete_note/<str:pk>', views.delete_note, name='delete'),
]