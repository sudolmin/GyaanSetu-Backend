from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User, TutorProfile, StudentProfile, JobPost, Review, Subjects

# Custom User admin
class UserAdmin(DefaultUserAdmin):
    list_display = ('username', 'email', 'is_tutor', 'is_student', 'is_staff', 'is_active')
    list_filter = ('is_tutor', 'is_student', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

# TutorProfile admin
class TutorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'skills', 'get_subjects', 'get_class_level', 'get_experience', 'get_metadata')
    search_fields = ('user__username', 'skills', 'subjects')
    list_filter = ('class_level',)
    
    def get_subjects(self, obj):
        return obj.subjects
    get_subjects.short_description = 'Subjects'
    
    def get_class_level(self, obj):
        return obj.class_level
    get_class_level.short_description = 'Class Level'
    
    def get_experience(self, obj):
        return obj.experience
    get_experience.short_description = 'Experience'
    
    def get_metadata(self, obj):
        return obj.metadata
    get_metadata.short_description = 'Metadata'

# StudentProfile admin
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'class_level', 'location')
    search_fields = ('user__username', 'subjects', 'class_level', 'location')

# JobPost admin
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'get_subjects', 'location', 'hourly_rate', 'currency', 'created_at', 'updated_at')
    search_fields = ('title', 'user__username', 'description', 'location')
    list_filter = ('location', 'subject')
    filter_horizontal = ('subject', 'viewed_by', 'interested')
    
    def get_subjects(self, obj):
        return ", ".join([subject.subject_name for subject in obj.subject.all()])
    get_subjects.short_description = 'Subjects'

# Review admin
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'review', 'rating', 'created_at', 'updated_at', 'tutor', 'student')
    search_fields = ('user__username', 'review', 'tutor__username', 'student__username')
    list_filter = ('rating',)

# Subjects admin
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'subject_code')
    search_fields = ('subject_name', 'subject_code')

# Registering models with custom admin
admin.site.register(User, UserAdmin)
admin.site.register(TutorProfile, TutorProfileAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(JobPost, JobPostAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Subjects, SubjectsAdmin)
