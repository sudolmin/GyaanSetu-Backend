# Generated by Django 5.0.7 on 2024-07-27 12:00

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(help_text='Name of the subject.', max_length=50)),
                ('subject_code', models.CharField(help_text='Code of the subject.', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_tutor', models.BooleanField(default=False, help_text='Indicates whether the user is a tutor.')),
                ('is_student', models.BooleanField(default=False, help_text='Indicates whether the user is a student.')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, help_text='The content of the review.', null=True)),
                ('rating', models.IntegerField(help_text='Rating given in the review.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the review was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Timestamp when the review was last updated.')),
                ('student', models.ForeignKey(help_text='The student who is being reviewed.', on_delete=django.db.models.deletion.CASCADE, related_name='student_reviews', to=settings.AUTH_USER_MODEL)),
                ('tutor', models.ForeignKey(help_text='The tutor who is being reviewed.', on_delete=django.db.models.deletion.CASCADE, related_name='tutor_reviews', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(help_text='The user who gave the review.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_level', models.CharField(help_text='Class level of the student.', max_length=50)),
                ('location', models.JSONField(blank=True, help_text='Location details for the job post.', null=True)),
                ('user', models.OneToOneField(help_text='The user associated with this profile.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subjects', models.ManyToManyField(help_text='Subjects the student is interested in.', related_name='student_subjects', to='core.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the job post.', max_length=100)),
                ('description', models.TextField(help_text='Description of the job post.')),
                ('location', models.JSONField(blank=True, help_text='Location details for the job post.', null=True)),
                ('hourly_rate', models.DecimalField(decimal_places=2, help_text='Hourly rate offered for the job.', max_digits=10)),
                ('currency', models.CharField(default='INR', help_text='Currency for the hourly rate.', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the job post was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Timestamp when the job post was last updated.')),
                ('accepted', models.ForeignKey(blank=True, help_text='User who has been accepted for the job post.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accepted_user', to=settings.AUTH_USER_MODEL)),
                ('interested', models.ManyToManyField(help_text='Users who have shown interest in the job post.', related_name='interested_users', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(help_text='The user who created the job post.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('viewed_by', models.ManyToManyField(help_text='Users who have viewed the job post.', related_name='viewed_users', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ManyToManyField(help_text='Subjects related to the job post.', related_name='job_post_subjects', to='core.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='TutorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.TextField(blank=True, help_text='Skills of the tutor.', null=True)),
                ('class_level', models.JSONField(blank=True, help_text='Class levels the tutor can teach, e.g., 1-5, 6-8, 9-10.', null=True)),
                ('experience', models.JSONField(blank=True, help_text='Experience details of the tutor, e.g., years of experience, number of students taught.', null=True)),
                ('metadata', models.JSONField(blank=True, help_text='Metadata about the tutor, e.g., preferred location, preferred time.', null=True)),
                ('subjects', models.ManyToManyField(help_text='Subjects the tutor can teach.', related_name='tutor_subjects', to='core.subjects')),
                ('user', models.OneToOneField(help_text='The user associated with this profile.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
