from django.contrib import messages
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


# Create your views here.

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):

        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        # 댓글 유효성 검사 (예: 내용이 비어 있지 않은지 확인)
        if not temp_comment.content.strip():
            messages.add_message(self.request, messages.ERROR, '댓글을 입력해주세요.')
            return self.form_invalid(form)
        temp_comment.save()

        # 성공 메시지 추가
        messages.add_message(self.request, messages.SUCCESS, '댓글이 작성되었습니다.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        # 댓글 삭제 로직
        response = super().delete(request, *args, **kwargs)

        # 성공 메시지 추가
        messages.add_message(request, messages.SUCCESS, '댓글이 삭제되었습니다.')
        return response

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})

