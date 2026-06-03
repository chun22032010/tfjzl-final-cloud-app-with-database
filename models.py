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

    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()
        selected_incorrect = self.choice_set.filter(is_correct=False, id__in=selected_ids).count()
        if all_answers == selected_correct and selected_incorrect == 0:
            return True
        return False

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class Enrollment(models.Model):
    user = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Learner(models.Model):
    user = models.CharField(max_length=100)

class Instructor(models.Model):
    user = models.CharField(max_length=100)

class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
