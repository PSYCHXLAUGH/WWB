from django.urls import path

from .views import *

urlpatterns = [
    path('', ContentListView.as_view(), name="home"),
    path('post/<slug:post_slug>/', PostDetailView.as_view(), name='post'),
    path('categories/<slug:cat_slug>/', CategoriesDetailView.as_view(), name='cat'),
    path('addpage/', PageCreateView.as_view(), name='addpage'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]
