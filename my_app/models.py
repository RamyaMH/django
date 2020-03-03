from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name + " " + self.emp_code


class Conference(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conference_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    topic = models.CharField(max_length=100)
    event_date = models.DateField()
    submission_end_date = models.DateField()
    publish_capacity = models.IntegerField()
    venue = models.CharField(max_length=100)
    cp = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Status(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status_id = models.AutoField(primary_key=True)
    status_code = models.IntegerField()
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name


class Article(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    authors = models.ManyToManyField(User)
    draft = models.TextField()
    original_paper = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_date = models.DateField()
    feedback = models.TextField()

