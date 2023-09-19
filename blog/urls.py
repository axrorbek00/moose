from django.urls import path
from .views import HomeView, BlogView, AboutView, ContactView, BlogDetailView, CommentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('detail/<str:slug>/', BlogDetailView.as_view(), name='detail'),
    path('comment/<str:slug>/', CommentView.as_view(), name='comment'),
]
