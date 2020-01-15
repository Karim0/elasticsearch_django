from django.shortcuts import render
from blog.documents import AppDocument, TagDocument
from .models import *


# Create your views here.


def search(request):
    query = request.GET.get('q', '')
    # print(query, 123)
    sqs_app = AppDocument.search().query("multi_match", query=query,
                                         fields=["name", "title", "abstract", "description"])
    sqs_tag = TagDocument.search().query("match", name=query)
    app = sqs_app.to_queryset()
    tag = sqs_tag.to_queryset()

    return render(request, 'index.html', {'apps': app, 'tags': tag})


def index(request):
    return render(request, "index.html", {})


def add(request):
    app = App()
    app.name = 'app'
    app.title = 'app'
    app.abstract = 'app'
    app.website = 'app'
    app.save()
    return render(request, "index.html", {})