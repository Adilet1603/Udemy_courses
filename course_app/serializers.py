from rest_framework import serializers
from .models import *


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ['network_name', 'network_link']


class UserProfileSerializer(serializers.ModelSerializer):
    user_networks = NetworkSerializer(read_only=True, many=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name',]




class CourseListSerializer(serializers.ModelSerializer):
    author = UserProfileSimpleSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'price',  'author']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['lesson', 'video', 'document']


class CourseDetailSerializer(serializers.ModelSerializer):
    author = UserProfileSimpleSerializer(many=True)
    category = CategoryListSerializer(many=True)
    update_date = serializers.DateTimeField(format = ('%d-%m-%Y %H:%M'))
    created_date = serializers.DateTimeField(format = ('%d-%m-%Y %H:%M'))
    lessons = LessonSerializer(read_only=True, many=True)
    class Meta:
        model = Course
        fields = ['id', 'course_name','category','price','description',
                  'certificate_have', 'course_lan', 'update_date', 'created_date',
                  'course_type', 'author']


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_courses = CourseListSerializer(read_only=True, many=True)


    class Meta:
        model = Category
        fields = ['category_name', 'category_courses']

class CourseUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'




# class LessonUpdateDestroySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lesson
#         fields = '__all__'
#
# #
# class LessonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lesson
#         fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['variant', 'check_var']

class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class QuestionListSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['question_name', 'score', 'options', ]


class ExamDetailSerializer(serializers.ModelSerializer):
    exam_questions = QuestionListSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ['exam_name ']







class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'





class ReviewSerializer(serializers.ModelSerializer):
    course = CourseListSerializer

    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'course_name', 'rating', 'comment']
