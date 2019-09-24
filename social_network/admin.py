from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from .models import Post

UserAdmin.list_display = ('username', 'email', 'is_active', 'date_joined', 'is_staff')

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'date')
    list_filter = ('date', 'body')
    search_fields = ('title', 'body')


admin.site.register(Post, PostAdmin)

