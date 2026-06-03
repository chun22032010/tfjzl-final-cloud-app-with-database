from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200, default="online course")
    image = models.ImageField(upload_to='courses/', null=True, blank=True)
    description = models.CharField(max_length=500)
    pub_date = models.DateField(null=True)

class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class Submission(models.Model):
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

class Enrollment(models.Model):
    user = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Learner(models.Model):
    user = models.CharField(max_length=100)

class Instructor(models.Model):
    user = models.CharField(max_length=100)
