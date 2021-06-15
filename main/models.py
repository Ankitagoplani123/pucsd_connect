from django.db import models


class Register(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.IntegerField()
    city = models.CharField(max_length=30)
    profile = models.OneToOneField("ProfileForm", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.profile)


class ProfileForm(models.Model):
    ROLES = (
        ('Alumni', 'Alumni'),
        ('Student', 'Student'),
        ('Faculty', 'Faculty')
    )
    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    CELL = (
        ('ALUMNI', 'Alumni Cell'),
        ('PLACEMENT', 'Placement Cell'),
        ('CSFG', 'CSFG Cell'),
        ('None', 'None')
    )
    MS = (
        ('Married', 'Married'),
        ('Single', 'Single')
    )
    role = models.CharField(max_length=30, choices=ROLES)
    gender = models.CharField(max_length=10, choices=SEX)
    course_start_year = models.IntegerField(blank=True)
    course_end_year = models.IntegerField(blank=True)
    cell = models.CharField(max_length=10, choices=CELL)
    alumni_data = models.OneToOneField("AlumniForm", on_delete=models.CASCADE, null=True, blank=True)
    achievements = models.CharField(max_length=100)
    highest_degree = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=10, choices=MS)

    def __str__(self):
        return "{} {}".format(self.role, self.course_start_year)


class AlumniForm(models.Model):
    first_company = models.CharField(max_length=20)
    current_company = models.CharField(max_length=20)
    experience = models.IntegerField()
    job_post = models.CharField(max_length=30)


class SpecialPostForm(models.Model):
    POST = (
        ('A', 'Administrator'),
        ('BM', 'Batch Manager'),
        ('CM', 'Course Manager'),
        ('F', 'Faculty')
    )
    post = models.CharField(max_length=2, choices=POST)
    profile = models.ManyToManyField("Register")
    batch_managing = models.IntegerField(blank=True, null=True)
    course_managing = models.CharField(max_length=20, blank=True, null=True)


class temp_model(models.Model):
    ROLES = (
        ('Alumni', 'Alumni'),
        ('Student', 'Student'),
        ('Faculty', 'Faculty')
    )
    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    CELL = (
        ('ALUMNI', 'Alumni Cell'),
        ('PLACEMENT', 'Placement Cell'),
        ('CSFG', 'CSFG Cell'),
        ('None', 'None')
    )
    MS = (
        ('Married', 'Married'),
        ('Single', 'Single')
    )

    role = models.CharField(max_length=30, choices=ROLES, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=SEX, blank=True, null=True)
    course_start_year = models.IntegerField(blank=True, null=True)
    course_end_year = models.IntegerField(blank=True, null=True)
    cell = models.CharField(max_length=10, choices=CELL, blank=True, null=True)
    marital_status = models.CharField(max_length=10, choices=MS, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    first_company = models.CharField(max_length=20, blank=True, null=True)
    current_company = models.CharField(max_length=20, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
