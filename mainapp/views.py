from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from mainapp.models import News


class IndexView(TemplateView):
    template_name = "mainapp/index.html"


class NewsView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = News.objects.filter(deleted=False)
        return context_data


class NewsDetail(TemplateView):
    template_name = 'mainapp/news_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object'] = get_object_or_404(News, pk=self.kwargs.get('pk'))
        return context_data


class CoursesView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSiteView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginView(TemplateView):
    template_name = "mainapp/login.html"
