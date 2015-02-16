from haystack import indexes
from .models import Illness


class IllnessENIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(model_attr='name', document=True, use_template=True, template_name="search/indexes/illness/illness_text.txt")

    def get_model(self):
        return Illness

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class IllnessSRIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(model_attr='name_sr', document=True, use_template=True, template_name="search/indexes/illness/illness_text_sr.txt")

    def get_model(self):
        return Illness

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()