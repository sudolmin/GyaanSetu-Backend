from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    User model extended from AbstractUser to include additional fields.
    """
    is_tutor = models.BooleanField(default=False, help_text="Indicates whether the user is a tutor.")
    is_student = models.BooleanField(default=False, help_text="Indicates whether the user is a student.")

class Subjects(models.Model):
    """
    Model to store information about subjects.
    """
    subject_name = models.CharField(max_length=50, help_text="Name of the subject.")
    subject_code = models.CharField(max_length=10, help_text="Code of the subject.")

    def __str__(self):
        return self.subject_name

class TutorProfile(models.Model):
    """
    Profile model for tutors.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="The user associated with this profile.")
    skills = models.TextField(null=True, blank=True, help_text="Skills of the tutor.")
    subjects = models.ManyToManyField(Subjects, related_name='tutor_subjects', help_text="Subjects the tutor can teach.")
    class_level = models.JSONField(null=True, blank=True, help_text="Class levels the tutor can teach, e.g., 1-5, 6-8, 9-10.")
    experience = models.JSONField(null=True, blank=True, help_text="Experience details of the tutor, e.g., years of experience, number of students taught.")
    metadata = models.JSONField(null=True, blank=True, help_text="Metadata about the tutor, e.g., preferred location, preferred time.")

    def __str__(self):
        return self.user.username

class StudentProfile(models.Model):
    """
    Profile model for students.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="The user associated with this profile.")
    subjects = models.ManyToManyField(Subjects, related_name='student_subjects', help_text="Subjects the student is interested in.")
    class_level = models.CharField(max_length=50, help_text="Class level of the student.")
    location = models.JSONField(null=True, blank=True, help_text="Location details for the job post.")                              # address, geo-coordinates etc.

    def __str__(self):
        return self.user.username

class JobPost(models.Model):
    """
    Model to store job posts created by students or tutors.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="The user who created the job post.")
    title = models.CharField(max_length=100, help_text="Title of the job post.")
    description = models.TextField(help_text="Description of the job post.")
    subject = models.ManyToManyField(Subjects, related_name='job_post_subjects', help_text="Subjects related to the job post.")
    location = models.JSONField(null=True, blank=True, help_text="Location details for the job post.")                              # address, geo-coordinates etc.
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, help_text="Hourly rate offered for the job.")
    currency = models.CharField(max_length=10, default='INR', help_text="Currency for the hourly rate.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the job post was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the job post was last updated.")
    
    viewed_by = models.ManyToManyField(User, related_name='viewed_users', help_text="Users who have viewed the job post.")
    interested = models.ManyToManyField(User, related_name='interested_users', help_text="Users who have shown interest in the job post.")
    accepted = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accepted_user', null=True, blank=True, help_text="User who has been accepted for the job post.")

    def __str__(self):
        return self.title

class Review(models.Model):
    """
    Model to store reviews given by users to tutors and students.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="The user who gave the review.")
    review = models.TextField(null=True, blank=True, help_text="The content of the review.")
    rating = models.IntegerField(help_text="Rating given in the review.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the review was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the review was last updated.")
    
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutor_reviews', help_text="The tutor who is being reviewed.")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_reviews', help_text="The student who is being reviewed.")

    def __str__(self):
        return f"Review by {self.user.username} - Rating: {self.rating}"
