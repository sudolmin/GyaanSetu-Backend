from django.urls import path
from .views import (
    UserCreate, UserDetail,
    TutorProfileCreate, TutorProfileDetail,
    StudentProfileCreate, StudentProfileDetail,
    JobPostCreate, JobPostList, JobPostDetail,
    ReviewCreate, ReviewList, ReviewDetail,
    SubjectsList, SubjectsDetail,
    MatchTutors
)

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-create'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),

    path('tutor-profile/', TutorProfileCreate.as_view(), name='tutor-profile-create'),
    path('tutor-profile/<int:pk>/', TutorProfileDetail.as_view(), name='tutor-profile-detail'),

    path('student-profile/', StudentProfileCreate.as_view(), name='student-profile-create'),
    path('student-profile/<int:pk>/', StudentProfileDetail.as_view(), name='student-profile-detail'),

    path('job-posts/', JobPostList.as_view(), name='job-post-list'),
    path('job-posts/create/', JobPostCreate.as_view(), name='job-post-create'),
    path('job-posts/<int:pk>/', JobPostDetail.as_view(), name='job-post-detail'),

    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/create/', ReviewCreate.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    path('subjects/', SubjectsList.as_view(), name='subjects-list'),
    path('subjects/<int:pk>/', SubjectsDetail.as_view(), name='subjects-detail'),

    path('match-tutors/', MatchTutors.as_view(), name='match-tutors'),
]
