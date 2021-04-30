from django.db import models


class Register(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.IntegerField()
    city = models.CharField(max_length=30)
    profile = models.OneToOneField("ProfileForm", on_delete=models.CASCADE,  null=True, blank=True)


class ProfileForm(models.Model):
    ROLES = (
        ('ALU', 'Alumni'),
        ('STU', 'Student'),
        ('FAC', 'Faculty')
    )
    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    CELL = (
        ('A', 'Alumni Cell'),
        ('P', 'Placement Cell'),
        ('C', 'CSFG Cell'),
        ('N', 'None')
    )
    MS = (
        ('M', 'Married'),
        ('S', 'Single')
    )
    role = models.CharField(max_length=3, choices=ROLES)
    gender = models.CharField(max_length=1, choices=SEX)
    course_start_year = models.IntegerField(blank=True)
    course_end_year = models.IntegerField(blank=True)
    cell = models.CharField(max_length=1, choices=CELL)
    alumni_data = models.OneToOneField("AlumniForm", on_delete=models.CASCADE, null=True, blank=True)
    achievements = models.CharField(max_length=100)
    highest_degree = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=1, choices=MS)

    def __str__(self):
        return self.role


class AlumniForm(models.Model):
    first_company = models.CharField(max_length=20)
    current_company = models.CharField(max_length=20)
    experience = models.IntegerField()
    job_post = models.CharField(max_length=30)


class SpecialPostForm(models.Model):
    POST = (
        ('S', 'Student'),
        ('A', 'Administrator'),
        ('BM', 'Batch Manager'),
        ('CM', 'Course Manager'),
        ('F', 'Faculty')
    )
    post = models.CharField(max_length=2, choices=POST)
    profile = models.ManyToManyField("ProfileForm")
    batch_managing = models.IntegerField(blank=True)
    course_managing = models.CharField(max_length=20, blank=True)
