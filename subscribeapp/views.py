from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from commentapp.models import Comment
from projectapp.models import Project
from subscribeapp.models import Subscription


# Create your views here.


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):

        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(user=user,
                                                   project=project)
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 8

    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)
        return article_list

    def get_context_data(self, **kwargs):
        # 기본 context 데이터 가져오기
        context = super().get_context_data(**kwargs)
        articles = context['article_list']

        # 각 게시글에 댓글 갯수 추가
        for article in articles:
            article.comment_count = Comment.objects.filter(article=article).count()

        # 수정된 게시글 리스트를 다시 context에 추가
        context['article_list'] = articles
        return context