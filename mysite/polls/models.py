from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        if (timezone.now() > self.pub_date):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        else:
            return False

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class AthleteProfile(models.Model):
    name = models.CharField(max_length=100)
    backsquat = models.IntegerField(default=0)
    deadlift = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def set_stat_value(self, stat_to_change, value):
        if stat_to_change == 'backsquat_value':
            self.backsquat = value
        elif stat_to_change == 'deadlift_value':
            self.deadlift = value

    def get_stat_value(self, stat_to_read):
        if stat_to_read == 'backsquat_value':
            value = self.backsquat
        elif stat_to_read == 'deadlift_value':
            value = self.deadlift

        return value
