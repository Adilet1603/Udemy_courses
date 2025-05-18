from .models import Category, Course, Network, Lesson
from modeltranslation.translator import register, TranslationOptions

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description', 'course_lan',)


@register(Network)
class NetworkTranslationOptions(TranslationOptions):
    fields = ('network_name',)


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('lesson',)
