from django.shortcuts import render, get_object_or_404
from .models import Music, Artist
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
# 리스트는 뷰 함수가 받을 메소드를 넣음
@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    # context = {'musics' : musics}
    # return render(request, 'music_list.html', context) 이건 옛날 방식 (html 페이지를 응답을 보내주기)
    # serialize가 된 걸 보내줄 것, 그래서 context가 필요 없음
    
    # 이 안에는 우리가 직렬화할 객체들을 넣어주면 됨
    # 음악들의 쿼리셋을 넣으면 알아서 json 파일을 만들어준다.
    serializer = MusicSerializer(musics, many=True)
    # render 함수 대신 Response 클래스를 리턴한다
    return Response(serializer.data)


# 데이터를 가져오니까 GET이다.
@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicDetailSerializer(music)
    return Response(serializer.data)

# 나중에는 둘 다 붙여줄 수 있음
# @api_view(['GET', 'POST'])
@api_view(['GET'])
def artist_list(request):
    artist = Artist.objects.all()
    # serializer = ArtistSerializer(artist, many=True)
    # 한 번에 여러 개 나오개 만듦
    serializer = ArtistDetailSerializer(artist, many=True)
    return Response(serializer.data)

# 이건 Read
@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

# 얘는 Create
@api_view(['POST'])
def comments_create(request, music_pk):
    # form = CommentForm(request.POST) 이것과 똑같다.
    # if form.is_valid():
    # POST나 GET으로 받는 것이 아니라, data로 받는다.
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # 잘못 들어오면 에러를 띠워줌
        serializer.save(music_id=music_pk)
    return Response(serializer.data)
