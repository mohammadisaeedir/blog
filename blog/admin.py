from django.contrib import admin
from .models import BlogOptions, Category, Post

# # Register your models here.


class BlogOptionsAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address', 'telegram')

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', '__str__', 'order',
                    'created_at', 'updated_at', 'slug')
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_special',
                    'created_at', 'updated_at', 'slug',)
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_special','category')


admin.site.register(BlogOptions, BlogOptionsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
