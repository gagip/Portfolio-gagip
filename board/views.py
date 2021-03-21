from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin           # 로그인 필요
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Board, Comment
from .forms import CommentForm

''' Geniric View를 사용하여 게시판 CRUD 구현 (CBV) '''

class BoardCreateView(LoginRequiredMixin, CreateView):
    ''' 게시글 작성 '''
    model = Board
    fields = ['title', 'text']
    template_name = 'board/board_upload.html'

    def form_valid(self, form):
        form.instance.author = self.request.user

        if form.is_valid():
            # 데이터가 올바른 경우
            post = form.save()
            return redirect(post)
        else:
            return self.render_to_response({'form':form})

class BoardListView(ListView):
    ''' 게시판 목록 조회 '''
    model = Board
    template_name = 'board/board_list.html'
    context_object_name = 'board_list'
    paginate_by = 5


class BoardDetailView(DetailView):
    ''' 게시글 상세조회 '''
    model = Board
    context_object_name = 'board'
    template_name = 'board/board_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm(auto_id=False)    # label 태그 안나오게
        return context

class BoardUpdateView(LoginRequiredMixin, UpdateView):
    ''' 게시글 수정 '''
    model = Board
    fields = ['title', 'text']
    template_name = 'board/board_update.html'

class BoardDeleteView(LoginRequiredMixin, DeleteView):
    ''' 게시글 삭제 '''
    model = Board
    success_url = 'blog:index'
    template_name = 'board/board_delete.html'


def search(request):
    ''' 검색 키워드 '''
    boards = Board.objects.all()

    q = request.GET.get('q', '')        # request 인자 중 q의 value가 없으면 빈 문자열 할당

    # q(검색어)가 존재하면 해당 내용을 가지는 게시판 제목 추출
    if q:
        boards = boards.filter(title__icontains=q)

    return render(request, 'board/board_list.html', {'board_list':boards})



# TODO FBV로 댓글 CRUD 구현
@login_required(login_url='member:login')
def comment_create(request, board_id):
    ''' 댓글 쓰기 '''
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        comment_form.instance.writer = request.user
        comment_form.instance.board_id = board_id
        
        if comment_form.is_valid():
            comment = comment_form.save()

    return HttpResponseRedirect(reverse_lazy('board:board_detail', args=[board_id]))

@login_required(login_url='member:login')
def comment_update(request, comment_id):
    ''' 댓글 수정 '''
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.writer:
        messages.error(request, '댓글 수정 권한이 없습니다.')
        return redirect('board:board_detail', board_id=comment.board.id)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('board:board_detail', board_id=comment.board.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form':form, 'board_id':comment.board.id}
    return render(request, 'board/comment_update.html', context)


@login_required(login_url='member:login')
def comment_delete(request, comment_id):
    ''' 댓글 삭제 '''
    comment = get_object_or_404(Comment, pk=comment_id)
    board_id = comment.board.id
    if request.user != comment.writer:
        messages.error(request, '댓글 삭제 권한이 없습니다.')
        return redirect('board:board_detail', pk=board_id)
    else:
        if request.method == 'POST':
            comment.delete()
            return redirect('board:board_detail', pk=board_id)
        else:
            return render(request, 'board/comment_delete.html', {'comment':comment})
    return redirect('board:board_detail', pk=board_id)