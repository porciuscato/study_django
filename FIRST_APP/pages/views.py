from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # request는 사용자가 보내온 인자들을 전달. 사용자가 보낸 요청들
    return render(request, 'index.html')

def home(request):
    # return HttpResponse('<h1>홈페이지</h1>')
    name = '이수진'
    data =['강동주','김지수','정의진']
    empty_data = ['엄복동','클레멘타인','성냥팔이소녀의 재림']
    matrix = [[1,2,3],[4,5,6]]
    # 혹은
    context = {
        'name': name,
        'data': data,
        'empty_data': empty_data,
        'matrix': matrix,
        'number': 10,
    }
    # return render(request, 'home.html',name=name,data=data) 이게 아니라
    return render(request, 'home.html',context) # 이런 식으로 하면 됨

def lotto(request):
    import random
    num = sorted(random.sample(range(1,46),6))
    context = {
        'lotto': num,
        'number': 10,
    }
    return render(request, 'lotto.html', context)

def cube(request, num):
    result= num*num*num
    context = {
        'result': result,
    }
    return render(request, 'cube.html',context)

def match(request):
    import random
    goonghap = random.randint(50,100)
    print(request)
    me = request.POST.get('me')
    you = request.POST.get('you')
    path = request.path_info
    test = request.get_host()
    req = request
    context = {
        'goonghap': goonghap,
        'me': me,
        'you': you,
        'path': path,
        'test': test,
        'req': request,
    }
    return render(request, 'match.html',context)