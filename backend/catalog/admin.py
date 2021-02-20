from django.contrib import admin
from .models import Genres, Author, Category, CategoryInstance

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pseudonym', 'last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', 'pseudonym', ('date_of_birth', 'date_of_death')]

admin.site.register(Genres)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('media_type', )
    list_display = ('title', 'author', 'year', 'display_genre', 'media_type')

    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'genre', 'media_type', 'year')
        }),
        ('Reference link', {
            'fields': ('link', )
        }),
        ('Optional', {
            'fields': ('image', )
        })
    )

@admin.register(CategoryInstance)
class CategoryInstanceAdmin(admin.ModelAdmin):
    list_filter = ('rating', 'category__media_type')
    list_display = ('category', 'get_pseudonym','get_first_name', 'get_last_name', 'get_year','get_type')
        
    fieldsets = (
        (None, {
            'fields': ('category', 'id')
        }),
        ('Rating', {
            'fields': ('rating', ) 
        }),
    )

    def get_type(self, obj):
        return obj.category.media_type
    get_type.admin_order_field  = 'media_type'

    def get_last_name(self, obj):
        return obj.category.author.last_name

    def get_first_name(self, obj):
        return obj.category.author.first_name

    def get_pseudonym(self, obj):
        return obj.category.author.pseudonym

    def get_year(self, obj):
        return obj.category.year