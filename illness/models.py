from django.db import models


class Illness(models.Model):
    name = models.CharField(max_length=1000, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, db_index=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural="Illnesses"