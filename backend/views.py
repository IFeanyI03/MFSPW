from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from app.serializers import SkillSerializer, DesignSerializer, ProjectSerializer, WorkedWithSerializer, ReportedErrorSerializer
from app.models import *
from rest_framework.pagination import PageNumberPagination

class SkillsView(ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class DesignsView(ListAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
    pagination_class = PageNumberPagination 
    page_size = 12

class ProjectsView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = PageNumberPagination 
    page_size = 8

class WorkedWithView(ListAPIView):
    queryset = WorkedWith.objects.all()
    serializer_class = WorkedWithSerializer
    
class ReportedErrorView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReportedErrorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
