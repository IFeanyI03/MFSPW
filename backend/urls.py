from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-skills/', SkillsView.as_view(), name='api_skills'),
    path('api-designs/', DesignsView.as_view(), name='api_designs'),
    path('api-projects/',ProjectsView.as_view(), name='api_Projects'),
    path('api-worked_withs/', WorkedWithView.as_view(), name='api_workwiths'),
    path('api-reported_errors/', ReportedErrorView.as_view(), name='api-report'),
    path('', include('app.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
