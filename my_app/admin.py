from django.contrib import admin
from .models import Employee, Position, Conference, Article, Status, Review

# Register your models here.
admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Conference)
admin.site.register(Article)
admin.site.register(Status)
admin.site.register(Review)