from django.contrib import admin
from .models import Category, Course, Network, Lesson, UserProfile, Exam, Question, Option, Certificate, Review
from modeltranslation.admin import TranslationAdmin


class NetworkInline(admin.TabularInline):
    model = Network
    extra = 1

class NetworkAdmin(admin.ModelAdmin):
    inlines = [NetworkInline]


@admin.register(Category, Course, Lesson)
class ProductAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile, NetworkAdmin)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Certificate)
admin.site.register(Review)
