import django
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin           # 로그인 필요
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Board
from .forms import CommentForm

''' Geniric View를 사용하여 게시판 CRUD 구현 (CBV) '''

class BoardCreateView(LoginRequiredMixin, CreateView):
    ''' 게시글 작성 '''
    model = Board
    fields = ['title', 'text']
    template_name = 'board/board_upload.html'

    def form_valid(self, form):
        form.instance.auther_id = self.request.user.id

        if form.is_valid():
            # 데이터가 올바른 경우
            form.instance.save()
            return redirect('blog:index')
        else:
            return self.render_to_response({'form':form})

class BoardListView(ListView):
    ''' 게시판 목록 조회 '''
    model = Board
    context_object_name = 'board_list'
    paginate_by = 10
    template_name = 'board/board_list.html'

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

# TODO FBV로 댓글 CRUD 구현 
@login_required
def comment_create(request, board_id):
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        comment_form.instance.writer = request.user
        comment_form.instance.board_id = board_id
        
        if comment_form.is_valid():
            comment = comment_form.save()

    return HttpResponseRedirect(reverse_lazy('board:board_detail', args=[board_id]))
