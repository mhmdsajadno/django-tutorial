from django.contrib import admin
from .models import Author, Book, BookAuthor, Publisher

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)
    ordering = ('name',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'published_date', 'get_authors', 'get_publishers')
    search_fields = ('name',)
    ordering = ('name',)

    def get_authors(self, obj):
        return ", ".join([author.author.name for author in obj.book_authors.all()])
    # get_authors.short_description = 'Authors'

    def get_publishers(self, obj):
        return ", ".join([publisher.name for publisher in obj.publisher.all()])
    get_publishers.short_description = 'Publishers'

class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('book', 'author')
    search_fields = ('book__name', 'author__name')
    ordering = ('book', 'author')

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
