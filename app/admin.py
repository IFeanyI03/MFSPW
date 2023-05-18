from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(WorkedWith)
admin.site.register(Project)
admin.site.register(Design)
admin.site.register(Skill)
admin.site.register(SkillType)
admin.site.register(ReportedError)