from typing import Any, Dict

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BlogModel
from .forms import CreateBlog


class LandingPage(generic.ListView):
    """ Load landing page """

    template_name = 'Blog/landing_page.html'
    model = BlogModel

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        articles = BlogModel.objects.all()

        context['articles'] = articles

        return context


class ArticlePage(generic.ListView):
    """ Main articles/blogs view """

    template_name = 'Blog/article.html'
    model = BlogModel

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)
        article_id = self.kwargs['article_id']
        article = BlogModel.objects.filter(id=article_id).first()

        context['article'] = article

        return context


class NewPostPage(LoginRequiredMixin, generic.edit.FormView):
    """ Create new post view """

    form_class = CreateBlog
    template_name = 'Blog/create_post.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('account')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()

        return context

    def form_valid(self, form: CreateBlog) -> Dict[str, Any]:
        data = form.cleaned_data

        article = BlogModel.objects.create(**data)
        article.owner = self.request.user
        article.save()

        return super().form_valid(form)

    def form_invalid(self, form: CreateBlog) -> Dict[str, Any]:
        messages.error(self.request, form.errors)

        return super().form_invalid(form)


class ArticleEditPage(LoginRequiredMixin, generic.edit.UpdateView):
    """ Edit blog/article page """

    template_name = 'Blog/article_edit.html'
    form_class = CreateBlog
    model = BlogModel
    redirect_authenticated_user = True
    success_url = reverse_lazy('account')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)
        article_id = self.kwargs['pk']
        article = BlogModel.objects.filter(id=article_id).first()
        form = self.form_class(
            self.request.POST or None,
            instance=article
        )

        context['form'] = form
        context['article'] = article

        return context
