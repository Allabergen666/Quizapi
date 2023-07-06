from django.db import models

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(max_length=500, verbose_name="Description")

    def __str__(self) -> str:
        return f"{self.title} {self.description}"

class Question(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    quiz = models.ForeignKey(Quiz, verbose_name="Quiz", on_delete=models.CASCADE, related_name="list_question")

    def __str__(self) -> str:
        return self.title

class Answer(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    question  = models.ForeignKey(Question, verbose_name="Question", on_delete=models.CASCADE, related_name="list_answers")
    is_correct = models.BooleanField(verbose_name="is_correct")

    def __str__(self) -> str:
        return f"{self.title} {self.is_correct}"
