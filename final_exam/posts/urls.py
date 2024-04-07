from django.urls import path

from final_exam.posts.views import PostListView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('create/', PostCreateView.as_view(), name='post_create'),
]
