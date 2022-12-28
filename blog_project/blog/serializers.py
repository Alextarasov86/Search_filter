from django.db.models import Q
from rest_framework import serializers
from .models import *
from users.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'

class ArticleUpdateSerializer(serializers.ModelSerializer):
    date_created = serializers.CharField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentUpdateSerializer(serializers.ModelSerializer):
    date_created = serializers.CharField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

class ArticleWithCommentsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    def get_comments(self, article):
        comments = Comment.objects.filter(article=article)
        return CommentSerializer(comments, many=True).data

    def get_author(self, article):
        return UserSerializer(article.author).data

    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'author', 'date_created', 'comments', 'is_published')

class CategorySerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()

    def get_articles(self, category):
        articles = Article.objects.filter(category=category)
        return ArticleSerializer(articles, many=True).data

    class Meta:
        model = Category
        fields = ('id', 'title', 'articles')


class CategoryWithArticlesSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()

    def get_articles(self, category):
        articles = Article.objects.filter(
            Q(category=category) | Q(category__parent=category)
        )
        return ArticleSerializer(articles, many=True).data

    class Meta:
        model = Category
        fields = ('id', 'title', 'parent', 'articles')

# class ArticleWithCategorySerializer(serializers.ModelSerializer):
#     categories = serializers.SerializerMethodField()
#
#     def get_categories(self, article):
#         categories = Category.objects.filter(article=article)
#         return CategorySerializer(categories).data
#
#     class Meta:
#         model = Article
#         fields = ('id', 'title', 'text', 'categories')