from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at','board', 'upvotes', 'downvotes', 'author']

    def create(self, validated_data):
        print(author)
        author = self.context['request'].user
        return Post.objects.create(author=author, **validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.upvotes = validated_data.get('upvotes', instance.upvotes)
        instance.downvotes = validated_data.get('downvotes', instance.downvotes)
        instance.board = validated_data.get('board', instance.board)
        instance.save()
        return instance
    