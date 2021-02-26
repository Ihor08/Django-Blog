from django.urls import path
from posts.views import posts_list, post_create, post_delete, post_detail, post_update

app_name = 'posts'

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('create/', post_create, name='post_create'),
    path('delete/<int:id>/', post_delete, name='post_delete'),
    path('detail/<int:id>/', post_detail, name='post_detail'),
    path('edit/<int:id>/', post_update, name='post_update'),
]
