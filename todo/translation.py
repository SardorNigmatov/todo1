from modeltranslation.translator import translator, TranslationOptions
from .models import ToDoModel

class NewsTranslationOptions(TranslationOptions):
    fields = ('task_name', 'task_description')

translator.register(ToDoModel, NewsTranslationOptions)