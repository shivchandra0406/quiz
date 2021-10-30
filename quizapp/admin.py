from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)


class AnswerAdmin(admin.StackedInline):
    model=Answerss
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerAdmin]
#admin.site.register(Question)
admin.site.register(Answerss)
