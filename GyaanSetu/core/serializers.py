from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import TutorProfile, StudentProfile, JobPost, Review, Subjects

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_tutor', 'is_student']

class TutorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorProfile
        fields = ['skills', 'subjects', 'class_level', 'experience', 'metadata']

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['subjects', 'class_level', 'location']

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ['id', 'user', 'title', 'description', 'subject', 'location', 'hourly_rate', 'currency', 'created_at', 'updated_at']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'review', 'rating', 'created_at', 'updated_at', 'tutor', 'student']

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['subject_name', 'subject_code']
