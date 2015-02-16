from django.views.generic import DetailView

from .models import Illness


class IllnessDetailView(DetailView):
    http_method_names = [u'get', u'post']
    model = Illness
    template_name = 'illness/detail_view.html'

    def get_slug_field(self):
        """
        Get the name of a slug field to be used to look up by slug.
        """
        return self.slug_field + '_' + self.request.LANGUAGE_CODE