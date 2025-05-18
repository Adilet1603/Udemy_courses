from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

router = SimpleRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'networks', NetworkViewSet)
router.register(r'options', OptionViewSet)
router.register(r'certificates', CertificateViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('courses/', CourseListAPIView.as_view(), name='course_list'),
    path('courses/create/', CourseCreateAPIView.as_view(), name='course_create'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('courses/<int:pk>/edit/', CourseUpdateDestroyAPIView.as_view(), name='course_update_delete'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/<int:pk>/', LessonUpdateDestroyAPIView.as_view(), name='lesson_update_delete'),
    path('reviews/<int:pk>/', ReviewAPIView.as_view(), name='reviews_list'),
    path('exams/', ExamListAPIView.as_view(), name='exam_list'),
    path('exams/<int:pk>/', ExamDetailAPIView.as_view(), name='exam_deatail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
