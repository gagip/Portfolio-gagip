from django.shortcuts import redirect, render
from django.contrib import auth
from .forms import SignupForm

def signup(request):
    ''' 회원가입 '''
    # 회원가입 입력 완료
    if request.method == "POST":
        user_form = SignupForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return redirect('blog:index')
            
    # 회원가입 입력 미완료. 회원가입 화면으로
    else:
        user_form = SignupForm()

    # 입력한 데이터를 'form'이라는 이름으로 보관 
    return render(request, 'member/signup.html', {'form':user_form})


def login(request):
    ''' 로그인 '''
    # 로그인 입력을 완료했을 시
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # 데이터 베이스(백앤드)에서 username과 pasword를 통해 사용자 인증
        user = auth.authenticate(request, username=username, password=password)

        # 해당 유저가 존재
        if user is not None:
            auth.login(request, user)
            return redirect('blog:index')
        # 해당 유저가 존재 X
        else:
            return render(request, 'member/login.html', {'error': '해당 유저가 존재하지 않습니다.'})
    # 로그인 항목 미입력. 로그인 화면 출력한다
    else:
        return render(request, 'member/login.html')

def logout(request):
    ''' 로그아웃 '''
    auth.logout(request)
    return redirect('blog:index')