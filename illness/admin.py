from django.contrib import admin
from .models import Illness


class IllnessAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",),
        "slug_en": ("name_en",),
        "slug_sr": ("name_sr",)
    }

admin.site.register(Illness, IllnessAdmin)
