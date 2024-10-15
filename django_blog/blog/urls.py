
# blog/urls.py
from django.urls import path
from . import views
from django.urls import path
from .views import post_detail, CommentCreateView, CommentUpdateView, CommentDeleteView
from django.urls import path
from .views import PostDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView, search_posts

urlpatterns = [
    path('posts/<int:pk>/', PostDetailView, name='post_detail'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),

    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('search/', search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
    
]

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]


urlpatterns = [
   
    # URL pattern for creating a new comment on a specific post
   
    # URL pattern for updating a specific comment
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
   
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    
    # URL pattern for deleting a specific comment
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    
    
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    
    # URL pattern for deleting a specific comment
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    
     # URL pattern for viewing the details of a specific post
    path('posts/<int:pk>/', PostDetailView, name='PostDetailView'),
    
]

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]

# blog/urls.py
from django.urls import path
from . import views
from django.urls import path
from .views import post_detail, CommentCreateView, CommentUpdateView, CommentDeleteView
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]

# blog/urls.py
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]


from django.urls import path
from .views import post_detail, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    # URL pattern for viewing details of a specific post
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    
    
    # URL pattern for updating a specific comment
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_edit'),
    
    # URL pattern for creating a new comment on a specific post
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    
    
    # URL pattern for deleting a specific comment
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]

urlpatterns = [
     path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),   
]