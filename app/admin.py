from django.contrib import admin
from .models import ReleaseYear, Theme, Article, Edition

admin.site.register(Article)
admin.site.register(Theme)
admin.site.register(ReleaseYear)
admin.site.register(Edition)
