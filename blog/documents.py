from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import App, Tag


@registry.register_document
class AppDocument(Document):
    class Index:
        name = 'apps'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    description = fields.TextField(attr='__str__')

    class Django:
        model = App
        fields = [
            'name',
            'title',
            'website',
            'abstract',
        ]


@registry.register_document
class TagDocument(Document):
    class Index:
        name = 'tags'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Tag
        fields = [
            'name',
            'identity',
        ]
