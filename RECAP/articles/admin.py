from django.contrib import admin
from .models import Article, Comment, Hashtag

# Register your models here.
# 이 안에는 모델이 들어간다

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
    # comma를 붙여줘야 가능
    list_display_links = ('title', )

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at',)

admin.site.register(Comment, CommentAdmin)

class HashtagAdmin(admin.ModelAdmin):
    list_display = ('content', )

admin.site.register(Hashtag, HashtagAdmin)