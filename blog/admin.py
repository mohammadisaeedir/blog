from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.safestring import mark_safe
# # Register your models here.


class BlogOptionsAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address', 'telegram')

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', '__str__', 'order',
                    'created_at', 'updated_at', 'slug', 'view_posts',)
    prepopulated_fields = {'slug': ('title',)}

    def view_posts(self, obj):
        count = obj.categories.count()
        return mark_safe('<a href="{}" target=blank>({}) Posts</a>'
                         .format(reverse("cat_page", args=(obj.slug,)), count))
    view_posts.short_description = 'Posts'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_special',
                    'created_at', 'updated_at', 'slug', 'get_view',)
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_special', 'category')
    filter_horizontal = ('posttag',)

    def get_view(self, obj):
        return mark_safe('<a href="{}" target=blank>{}</a>'.format(reverse("post_page", args=(obj.slug,)), obj.slug))
    get_view.short_description = 'View'
    

class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'slug',
                    'get_absolute_url', 'post_link',)
    prepopulated_fields = {'slug': ('title',)}

    def post_link(self, obj):
        count = obj.tags.count()
        return mark_safe('<a href="{}" target=blank>({}) Posts</a>'.format(
            reverse("tag_page", args=(obj.slug,)), count
        ))
    post_link.short_description = 'Posts'


admin.site.register(BlogOptions, BlogOptionsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
