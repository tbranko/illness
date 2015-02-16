from modeltranslation.translator import translator, TranslationOptions
from .models import Illness


class IllnessTranslationOptions(TranslationOptions):
    fields = ("name", "slug")

translator.register(Illness, IllnessTranslationOptions)