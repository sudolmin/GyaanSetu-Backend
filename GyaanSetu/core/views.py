from rest_framework import generics
from django.contrib.auth import get_user_model
from .models import TutorProfile, StudentProfile, JobPost, Review, Subjects
from .serializers import UserSerializer, TutorProfileSerializer, StudentProfileSerializer, JobPostSerializer, ReviewSerializer, SubjectsSerializer

User = get_user_model()

# User views
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Profile views
class TutorProfileCreate(generics.CreateAPIView):
    queryset = TutorProfile.objects.all()
    serializer_class = TutorProfileSerializer

class StudentProfileCreate(generics.CreateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

class TutorProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = TutorProfile.objects.all()
    serializer_class = TutorProfileSerializer

class StudentProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

# Job Post views
class JobPostCreate(generics.CreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

class JobPostList(generics.ListAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

class JobPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

# Review views
class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Subjects views
class SubjectsList(generics.ListCreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer

class SubjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer

# Matching Tutors
class MatchTutors(generics.ListAPIView):
    serializer_class = TutorProfileSerializer

    def get_queryset(self):
        subjects = self.request.query_params.get('subjects', None)
        location = self.request.query_params.get('location', None)
        queryset = TutorProfile.objects.all()
        if subjects:
            queryset = queryset.filter(subjects__icontains=subjects)
        if location:
            queryset = queryset.filter(metadata__location__icontains=location)
        return queryset
