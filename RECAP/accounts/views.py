from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from IPython import embed
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm

# Create your views here.
def signup(request):
    if not request.user.is_anonymous:
        return redirect('articles:index')
    if request.method == 'POST':
        # 실제 DB에 정보 저장
        form = UserCreationForm(request.POST)
        # embed()
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/auth_form.html', context)

# 함수 안에 함수를 넣는 것. 이 함수를 돌리기 전에 이걸 하라는 뜻
# @login_require
def login(request):
    # 만약 로그인 되어있으면 articles의 index로 돌려보내자
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        # 로그인시키려면 로그인하는 것에 대한 모든 정보가 필요하기 때문에 request를 함
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 시킨다.
            # username = request.POST.get('username')
            # user = User.objects.get(username=username)
            auth_login(request, form.get_user())
            # if request.GET.get('next'):
            #     return redirect(request.GET.get('next'))
            # else:
            #     return redirect('articles:index')
            return redirect(request.GET.get('next') or 'articles:index')
            
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/auth_form.html', context)


def logout(request):
    # 세션을 지우기
    auth_logout(request)
    return redirect('articles:index')

@require_POST
@login_required
def delete(requests):
    # DB에서 user를 삭제한다.
    # user = User.objects.get(pk=requets.user.pk)
    # user.delete()
    requests.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        # 실제 DB에 적용
        # 인자 하나가 오면 새로 생성, 둘이 오면 수정임을 안다.
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # 편집 화면 보여줌 
        form = CustomUserChangeForm(instance=request.user)
        context = {
            'form' : form,
        }
        return render(request, 'accounts/auth_form.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # session auth hash가 변경되면서 기존의 유저와 다르다고 인식
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        # 편집 화면 보여줌(form)
        form = PasswordChangeForm(request.user)
        context = {
            'form' : form,
        }
        return render(request, 'accounts/auth_form.html', context)