from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employee, Position, Article, Status, Conference, Review


class EmployeeSerializer(serializers.ModelSerializer):
    # position = PositionSerializer
    class Meta:
        model = Employee
        fields = ('full_name', 'emp_code', 'mobile', 'position'
                  )
        depth = 1


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('title'
                  )


class UserSerializer(serializers.ModelSerializer):
    user_groups = serializers.SerializerMethodField('get_groups')

    def get_groups(self, user):
        return user.groups.values_list('name', flat=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined',
            'last_login',
            'is_staff',
            'is_superuser',
            'is_active',
            'user_groups'
        ]


class ArticleSerializer(serializers.ModelSerializer):
    original_paper = serializers.FileField(max_length=None, use_url=True, required=False)
    # icon = serializers.FileField(source='details_sample.icon', required=False)

    class Meta:
        model = Article
        fields = [
            'article_id',
            'title',
            'conference',
            'status',
            'authors',
            'draft',
            'original_paper'
        ]


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'status_id',
            'status_code',
            'status_name'
        ]


class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = [
            'conference_id',
            'name',
            'description',
            'topic',
            'event_date',
            'submission_end_date',
            'publish_capacity',
            'venue',
            'cp'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'article',
            'reviewer',
            'submitted_date',
            'feedback'
        ]
