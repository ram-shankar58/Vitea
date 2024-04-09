from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=['id','title','content','description','created_at','updated_at','club']

        def create(self, validated_data):
            print(club)
            club=self.context['request'].user
            return Event.objects.create(club=club, **validated_data)
        

        def update(self, instance, validated_data):
            instance.title=validated_data.get('title', instance.title)
            instance.content=validated_data.get('content', instance.content)
            instance.description=validated_data.get('description', instance.description)

            instance.save()

            return instance


