from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.IndexView.as_view()),
    path("news.html", views.NewsView.as_view()),
    path("courses_list/", views.CoursesView.as_view()),
    path("contacts/", views.ContactsView.as_view()),
    path("doc_site/", views.DocSiteView.as_view()),
    path("login/", views.LoginView.as_view()),
]
