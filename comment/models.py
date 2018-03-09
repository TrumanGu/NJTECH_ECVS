from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_name = models.CharField(max_length=32)
    user_id = models.CharField(max_length=32)
    use_grade = models.IntegerField()
    def __str__(self):
        return self.user_name

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=32)

    def __str__(self):
        return self.teacher_name




class Subject(models.Model):
    subject_name = models.CharField(max_length=32)
    subject_comments = models.TextField(null=True)
    subject_grade = models.IntegerField(null=True)
    subject_stars = models.FloatField(null=True)
    subject_teacher = models.ForeignKey(Teacher, on_delete='CASCADE')

    def __str__(self):
        return self.subject_name



