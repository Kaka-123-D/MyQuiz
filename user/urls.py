from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('student_dashboard/', views.student_dashboard, name = 'student_dashboard'),
    path('teacher_dashboard/', views.teacher_dashboard, name = 'teacher_dashboard'),
    path('pack/', views.unregistered_quizpack_list_view, name = 'all_quizpack'),
    path('pack/add/<int:id>', views.register_quizpack_view, name = 'register_pack'),
    path('pack/remove/<int:id>/', views.unregister_quizpack_view, name = 'unregister_pack'),
    path('teacher_dashboard/courses/new_course', views.create_new_course),
    path('courses_list/', views.show_courses_list, name='courses'),
    path('courses_list/<int:id>/', views.course_data, name='course_data'),
]
