from django.contrib import admin
from .models import Author, Category, Tag, Series, Post, PostImage

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "bio", "email", "slug",]
    search_fields = ["name",]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug",]
    search_fields = ["name",]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "slug",]


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ["title",]


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ["image",]


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "category",
                    "series", "status", "published_at",]
    inlines = [PostImageInline]
