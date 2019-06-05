from django.contrib import admin

# Register your models here.
from .models import BookInfo, HeroInfo

class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 2

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10
    fieldsets = [
    ('basic',{'fields': ['btitle']}),
    ('more', {'fields': ['bpub_date']}),
    ]

    inlines = [HeroInfoInline]

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)