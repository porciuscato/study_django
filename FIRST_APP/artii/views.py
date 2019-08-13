from django.shortcuts import render
import requests

# Create your views here.

def artii(request):
    return render(request, 'artii/artii.html')

def result(request):
    #  1. 단어를 받아온다.
    input_word = request.GET.get('word')
    # 2. artii api를 통해 받아온다.
    url = 'http://artii.herokuapp.com/make?text='
    result = requests.get('{}{}'.format(url,input_word)).text

    context = {
        'word': input_word,
        "result": result,
    }
    return render(request, 'artii/artii_result.html',context)