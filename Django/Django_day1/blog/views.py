from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
from blog.models import Article


def index(request: HttpRequest):
    qs = Article.objects.all()
    return render(request, "blog/Article_list.html", {
        "Article_list": qs,
    })

def article_detail(request: HttpRequest, pk: int):
    article = Article.objects.get(pk=pk)
    return render(request, "blog/article_detail.html", {
        "article": article,
    })