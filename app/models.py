from django.db import models

# Create your models here.

class WorkedWith(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name
    

class Project(models.Model):
    name = models.CharField(max_length=20)
    info= models.TextField(max_length=500)
    mobile_preview = models.ImageField(null=True, blank=True, upload_to="images/")
    tab_preview = models.ImageField(null=True, blank=True, upload_to="images/")
    pc_preview = models.ImageField(null=True, blank=True, upload_to="images/")
    p_link = models.URLField(max_length=100)
    github_link = models.URLField(max_length=100)
    worked_with = models.ManyToManyField(WorkedWith)
    p_type = models.CharField(max_length=20, null=True, blank=True)
    worked_on = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Design(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    info = models.TextField(max_length=500, null=True, blank=True)
    worked_with = models.ManyToManyField(WorkedWith)
    
    def __str__(self):
        return self.name

class SkillType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Skill(models.Model):
    level_choice = [
        ( 40 , 'Beginner' ),
        ( 75, 'Intermediate' ),
        ( 95, 'Advance' )
    ]
    name = models.CharField(max_length=20)
    level = models.IntegerField(null=True, blank=True, choices=level_choice)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    skill_type = models.ManyToManyField(SkillType)
    color = models.CharField(max_length=6, null=True, blank=True)
    
    def __str__(self):
        return self.name


class ReportedError(models.Model):
    err_choice = [
        ('Layout', 'Layout'),
        ('Animation', 'Animation'),
        ('Links', 'Link'),
        ('Option not available', 'Option not available')
    ]
    choice = models.CharField(max_length=20, choices=err_choice, null=True, blank=True)
    description = models.TextField(max_length=500)
    d_width = models.IntegerField()
    d_height = models.IntegerField()
    err_section = models.CharField(max_length=15, null=True, blank=True)

