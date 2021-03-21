from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, ProfileForm, CheckPasswordForm 
from .models import Profile

def signup(request):
    ''' 회원가입 '''
    # 회원가입 입력 완료
    if request.method == "POST":
        user_form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        try:
            new_user = user_form.save(commit=False)
            new_profile = profile_form.save(commit=False)
        except:
            pass
            # return 에러 
        if user_form.is_valid() and profile_form.is_valid():
            new_user.set_password(user_form.cleaned_data['password'])
            
            profile_form.instance.user = new_user
            new_user.save()
            profile_form.save()

            auth.login(request, new_user)
            return redirect('blog:index')
            
    # 회원가입 입력 미완료. 회원가입 화면으로
    else:
        user_form = SignupForm()
        profile_form = ProfileForm()

    # 입력한 데이터를 'form'이라는 이름으로 보관 
    return render(request, 'member/signup.html', {'form':user_form, 'profile_form':profile_form})


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

@login_required
def logout(request):
    ''' 로그아웃 '''
    auth.logout(request)
    return redirect('blog:index')


def profile(request, user_id):
    ''' 프로필 '''
    # https://tothefullest08.github.io/django/2019/06/20/Django25_relations4_OneToOne_Profile/
    try:
        member = User.objects.get(pk=user_id)
    except:
        print('해당 유저가 존재하지 않습니다.')

    return render(request, 'member/profile.html', {'member':member})

@login_required
def member_delete(request):
    ''' 회원 탈퇴 '''
    if request.method == "POST":
        password_form = CheckPasswordForm(request.user, request.POST)

        # 타당성 검사 후 회원 탈퇴
        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('blog:index')
    
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'member/member_delete.html', {'password_form': password_form})


@login_required
def profile_update(request):
    ''' 프로필 변경 '''
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile = profile_form.save()
            return redirect('member:profile', user_id=request.user.id)        

    else:
        profile_form = ProfileForm(instance=profile)

    return render(request, 'member/profile_update.html', {'profile_form':profile_form})