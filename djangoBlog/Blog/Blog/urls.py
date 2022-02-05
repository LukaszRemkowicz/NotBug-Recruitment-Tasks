from django.contrib import admin
from django.urls import path

from .views import LandingPage, ArticlePage, ArticleEditPage, NewPostPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name='landing_page'),
    path('new_post/', NewPostPage.as_view(), name='add_new_post'),
    path('article/<int:pk>/edit', ArticleEditPage.as_view(), name='article-edit-page'),
    path('article/<int:article_id>', ArticlePage.as_view(), name='article-page'),
]
