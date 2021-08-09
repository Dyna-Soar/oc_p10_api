from django.db import models
from rest_framework import permissions
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """User class"""
    pass


class Contributor(models.Model):
    """Contributor class"""
    user_id = models.ManyToManyField(User)
    project_id = models.IntegerField()
    # permission is ChoiceField (choice=...)
    permission = models.CharField(max_length=150)
    role = models.CharField(max_length=150)


class Project(models.Model):
    """Project class"""
    project_id = models.IntegerField()
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=150)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Issue(models.Model):
    """Issue class"""
    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=150)
    tag = models.CharField(max_length=150)
    priority = models.CharField(max_length=150)
    project_id = models.IntegerField()
    status = models.CharField(max_length=150)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_issue")
    assignee_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assignee_issue")
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    """Comment class"""
    comment_id = models.IntegerField()
    description = models.CharField(max_length=150)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateField(auto_now_add=True)
