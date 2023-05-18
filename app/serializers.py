from rest_framework import serializers
from .models import *

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            'name', 'level', 'image', 'skill_type', 'color'
        ]

class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = [
            'name', 'info', 'image', 'worked_with'
        ]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'name', 'info', 'mobile_preview', 'tab_preview', 'pc_preview', 'p_link', 'github_link', 'worked_with', 'p_type', 'worked_on'
        ]


class WorkedWithSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkedWith
        fields = [
            'name', 'logo'
        ]


class ReportedErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportedError
        fields = [
            'description', 'd_width', 'd_height', 'choice', 'err_section'
        ]