from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.first_name:
            raise forms.ValidationError("First name needed......")
        super().save_model(request, obj, form, change)
    list_display = [
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "groups",
                    "first_name",
                    "last_name",
                    "email",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )
    ordering = ("id",)
    search_fields = ['username']
admin.site.register(CustomUser, CustomUserAdmin)
