"""" Polls application
Question : Thông tin của question
Choice: lựa chọn cho question. Mỗi question có nhiều choice, một choice dùng cho một question



"""
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.



class Question(models.Model):
    """" Thông tin của question
    question_text: Nội dung của question
    pub_date: thời gian question được publish


    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # date published human readable.
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    """"
    question: Question có quan hệ với choice
    choice_text: Mô tả về choice
    votes: đếm số lần choice được lựa chon
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

    