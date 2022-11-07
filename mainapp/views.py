from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime


class IndexView(TemplateView):
    template_name = "mainapp/index.html"


class NewsView(TemplateView):
    template_name = "mainapp/news.html"

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    # как вариант
    # context_data['object_list'] = [
    #     {
    #         'title': 'Новость',
    #         'preview': 'Скандалы, интриги, расследования',
    #         'data': datetime.now()
    #     }, {
    #         'title': 'Новость',
    #         'preview': 'Скандалы, интриги, расследования',
    #         'data': datetime.now()
    #     }, {
    #         'title': 'Новость три',
    #         'preview': 'Скандалы, интриги, расследования',
    #         'data': datetime.now()
    #     }, {
    #         'title': 'Новость четыре',
    #         'preview': 'Скандалы, интриги, расследования',
    #         'data': datetime.now()
    #     }, {
    #         'title': 'Новость пять',
    #         'preview': 'Скандалы, интриги, расследования',
    #         'data': datetime.now()
    #     },
    # ]
    # return context_data
    # как вариант, но покороче
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Новость"
        context["preview"] = "Скандалы, интриги, расследования"
        context["date"] = datetime.now()
        context["range"] = range(5)
        return context


class CoursesView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSiteView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginView(TemplateView):
    template_name = "mainapp/login.html"
