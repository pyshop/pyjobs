from haystack import indexes
from .models import Advert


class AdvertIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)

    title = indexes.EdgeNgramField(model_attr='title')
    author = indexes.EdgeNgramField(model_attr='author')
    timestamp = indexes.DateTimeField(model_attr='timestamp')
    description = indexes.EdgeNgramField(model_attr='description')
    city = indexes.EdgeNgramField(model_attr='city')
    requirements = indexes.EdgeNgramField(model_attr='requirements')
    salary = indexes.EdgeNgramField(model_attr='salary')
    is_remote = indexes.BooleanField(model_attr='is_remote')

    def get_model(self):
        return Advert

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
