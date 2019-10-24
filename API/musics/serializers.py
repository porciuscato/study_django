from rest_framework import serializers
from .models import Music, Artist, Comment


# forms.ModelForm

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('pk', 'title', 'artist_id',)


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('pk', 'name',)

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True)
    class Meta(ArtistSerializer.Meta):
        # 상속을 쓰는 방법
        fields = ArtistSerializer.Meta.fields + ('music_set', )
    # 코드가 너무 기니까 다시 정의해도 상관 없음
    # 그러나 코드 중복을 허용하지 않기에 위 방식이 선호된다.


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = ('pk', 'content', 'music')
        fields = ('pk', 'music_id', 'content',)


class MusicDetailSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(source='comment_set', many=True)
    comment_set = CommentSerializer(many=True)
    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ('comment_set',)


# forms.Form
# serializer는 그냥 json 파일만 만들어주고
# ModelSerializer는 모델을 자기가 알아서 json으로 만들어줌
# forms.ModelForm