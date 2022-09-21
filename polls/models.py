from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')   # админ панель видит как 'date published' (verbose_name)

    def __str__(self):
        return self.question_textq


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
