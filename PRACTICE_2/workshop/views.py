from django.shortcuts import render

# Create your views here.
def push_number(request):
    return render(request, 'push_number.html')


def pull_number(request):
    num = request.GET.get('number')
    result = 'Pull 해보니 {} 입니다!'.format(num)
    context = {
        "result": result,
    }
    return render(request, 'pull_number.html', context)