from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, Product, Message, Review
from django.urls import reverse
from django.http import HttpResponseRedirect


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['username', 'email', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_pic',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('profile_pic', )}),
    )


class MyAdminSite(admin.AdminSite):
    def index(self, request, extra_context=None):
        # Redirect Django admin homepage to your dashboard
        return HttpResponseRedirect(reverse("staff_dashboard"))


admin_site = MyAdminSite(name="myadmin")


# ✅ Product admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_public', 'is_sold', 'seller', 'posted_at')
    list_filter = ('is_public', 'is_sold', 'posted_at', 'seller')
    search_fields = ('title', 'description', 'seller__username')
    ordering = ('-posted_at',)
    list_display_links = ('title',)


# ✅ Review admin
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('comment', 'author__username', 'product__title')


# ✅ Message admin
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'subject', 'sent_at', 'is_read')
    list_filter = ('is_read', 'sent_at')
    search_fields = ('subject', 'body', 'sender__username', 'receiver__username')


# ✅ CustomUser admin
admin.site.register(CustomUser, CustomUserAdmin)
