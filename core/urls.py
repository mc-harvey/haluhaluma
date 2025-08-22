# core/urls.py

from django.urls import path
from . import views
from .admin import admin_site
from .views import (
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    InboxView, SendMessageView, MessageDetailView,  # Removed SentMessagesView
    delete_conversation_view, staff_dashboard
)

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('', views.base, name='base'),

    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/category/<str:category_name>/', ProductListView.as_view(), name='category_list'),

    # Messaging URLs
    path('messages/inbox/', InboxView.as_view(), name='inbox'),
    # REMOVED: path('messages/sent/', SentMessagesView.as_view(), name='sent_messages'),
    path('messages/send/', SendMessageView.as_view(), name='message_send'),
    path('messages/send/<int:recipient_pk>/', SendMessageView.as_view(), name='message_send_to_user'),
    path('messages/reply/<int:parent_pk>/', SendMessageView.as_view(), name='message_reply'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),

    path('messages/<int:pk>/delete/', views.delete_conversation_view, name='delete_conversation'),

    path('product/<int:pk>/add_review/', views.add_review, name='add_review'),

    # NEW URL to handle review deletion
    path('review/<int:pk>/delete/', views.delete_review, name='delete_review'),

    # Help and FAQ URL
    path('help/', views.help_view, name='help'),

    # ADMIN DASHBOARD    path("admin/", admin_site.urls),  # Django admin, but home redirects
    path("staff/dashboard/", views.staff_dashboard, name="staff_dashboard"),
    path("staff/users/", views.user, name="user"),
    path("staff/product/", views.product, name="product"),



]