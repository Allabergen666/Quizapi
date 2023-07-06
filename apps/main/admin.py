from django.contrib import admin
from .models import Quiz, Question, Answer
# Register your models here.

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Answer)
class Answerdmin(admin.ModelAdmin):
    list_display = ['title', 'is_correct']
