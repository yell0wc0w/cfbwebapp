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

    snatch_1rm = models.IntegerField(default=0)
    power_snatch_1rm = models.IntegerField(default=0)
    hang_snatch_1rm = models.IntegerField(default=0)
    squat_snatch_1rm = models.IntegerField(default=0)

    clean_and_jerk_1rm = models.IntegerField(default=0)

    hang_clean_1rm = models.IntegerField(default=0)
    power_clean_1rm = models.IntegerField(default=0)
    squat_clean_1rm = models.IntegerField(default=0)

    split_jerk_1rm = models.IntegerField(default=0)
    push_jerk_1rm = models.IntegerField(default=0)
    push_press_1rm = models.IntegerField(default=0)
    shoulder_press_1rm = models.IntegerField(default=0)

    backsquat_1rm = models.IntegerField(default=0)
    backsquat_3rm = models.IntegerField(default=0)
    backsquat_5rm = models.IntegerField(default=0)

    front_squat_1rm = models.IntegerField(default=0)
    front_squat_3rm = models.IntegerField(default=0)
    front_squat_5rm = models.IntegerField(default=0)

    deadlift_1rm = models.IntegerField(default=0)
    deadlift_3rm = models.IntegerField(default=0)
    deadlift_5rm = models.IntegerField(default=0)

    angie = models.CharField(max_length=10, default='0')
    barbara = models.CharField(max_length=10, default='0')
    chelsea = models.CharField(max_length=10, default='0')
    cindy = models.CharField(max_length=10, default='0')
    diane = models.CharField(max_length=10, default='0')
    elizabeth = models.CharField(max_length=10, default='0')
    fran = models.CharField(max_length=10, default='0')
    grace = models.CharField(max_length=10, default='0')
    nicole = models.CharField(max_length=10, default='0')
    helen = models.CharField(max_length=10, default='0')
    isabel = models.CharField(max_length=10, default='0')
    jackie = models.CharField(max_length=10, default='0')
    karen = models.CharField(max_length=10, default='0')
    mary = models.CharField(max_length=10, default='0')
    nancy = models.CharField(max_length=10, default='0')
    annie = models.CharField(max_length=10, default='0')
    eva = models.CharField(max_length=10, default='0')
    kelly = models.CharField(max_length=10, default='0')
    jt = models.CharField(max_length=10, default='0')
    michael = models.CharField(max_length=10, default='0')
    murph = models.CharField(max_length=10, default='0')
    daniel = models.CharField(max_length=10, default='0')
    josh = models.CharField(max_length=10, default='0')
    filthy50 = models.CharField(max_length=10, default='0')
    badger = models.CharField(max_length=10, default='0')
    nate = models.CharField(max_length=10, default='0')
    randy = models.CharField(max_length=10, default='0')
    tommy_v = models.CharField(max_length=10, default='0')
    ryan = models.CharField(max_length=10, default='0')
    mr_joshua = models.CharField(max_length=10, default='0')
    dt = models.CharField(max_length=10, default='0')
    danny = models.CharField(max_length=10, default='0')
    the_seven = models.CharField(max_length=10, default='0')
    lumberjack20 = models.CharField(max_length=10, default='0')
    mcghee = models.CharField(max_length=10, default='0')
    jack = models.CharField(max_length=10, default='0')
    bulger = models.CharField(max_length=10, default='0')
    fight_gone_bad = models.CharField(max_length=10, default='0')

    stats_dict = {}

    def __str__(self):
        return self.name

    def setup_stats(self):
        self.stats_dict['snatch_1rm'] = self.snatch_1rm
        self.stats_dict['power_snatch_1rm'] = self.power_snatch_1rm
        self.stats_dict['hang_snatch_1rm'] = self.hang_snatch_1rm
        self.stats_dict['squat_snatch_1rm'] = self.squat_snatch_1rm

        self.stats_dict['clean_and_jerk_1rm'] = self.clean_and_jerk_1rm

        self.stats_dict['hang_clean_1rm'] = self.hang_clean_1rm
        self.stats_dict['power_clean_1rm'] = self.power_clean_1rm
        self.stats_dict['squat_clean_1rm'] = self.squat_clean_1rm

        self.stats_dict['split_jerk_1rm'] = self.split_jerk_1rm
        self.stats_dict['push_jerk_1rm'] = self.push_jerk_1rm
        self.stats_dict['push_press_1rm'] = self.push_press_1rm
        self.stats_dict['shoulder_press_1rm'] = self.shoulder_press_1rm

        self.stats_dict['backsquat_1rm'] = self.backsquat_1rm
        self.stats_dict['backsquat_3rm'] = self.backsquat_3rm
        self.stats_dict['backsquat_5rm'] = self.backsquat_5rm

        self.stats_dict['front_squat_1rm'] = self.front_squat_1rm
        self.stats_dict['front_squat_3rm'] = self.front_squat_3rm
        self.stats_dict['front_squat_5rm'] = self.front_squat_5rm

        self.stats_dict['deadlift_1rm'] = self.deadlift_1rm
        self.stats_dict['deadlift_3rm'] = self.deadlift_3rm
        self.stats_dict['deadlift_5rm'] = self.deadlift_5rm

        self.stats_dict['angie'] = self.angie
        self.stats_dict['barbara'] = self.barbara
        self.stats_dict['chelsea'] = self.chelsea
        self.stats_dict['cindy'] = self.cindy
        self.stats_dict['diane'] = self.diane
        self.stats_dict['elizabeth'] = self.elizabeth
        self.stats_dict['fran'] = self.fran
        self.stats_dict['grace'] = self.grace
        self.stats_dict['nicole'] = self.nicole
        self.stats_dict['helen'] = self.helen
        self.stats_dict['isabel'] = self.isabel
        self.stats_dict['jackie'] = self.jackie
        self.stats_dict['karen'] = self.karen
        self.stats_dict['mary'] = self.mary
        self.stats_dict['nancy'] = self.nancy
        self.stats_dict['annie'] = self.annie
        self.stats_dict['eva'] = self.eva
        self.stats_dict['kelly'] = self.kelly
        self.stats_dict['jt'] = self.jt
        self.stats_dict['michael'] = self.michael
        self.stats_dict['murph'] = self.murph
        self.stats_dict['daniel'] = self.daniel
        self.stats_dict['josh'] = self.josh
        self.stats_dict['filthy50'] = self.filthy50
        self.stats_dict['badger'] = self.badger
        self.stats_dict['nate'] = self.nate
        self.stats_dict['randy'] = self.randy
        self.stats_dict['tommy_v'] = self.tommy_v
        self.stats_dict['ryan'] = self.ryan
        self.stats_dict['mr_joshua'] = self.mr_joshua
        self.stats_dict['dt'] = self.dt
        self.stats_dict['danny'] = self.danny
        self.stats_dict['the_seven'] = self.the_seven
        self.stats_dict['lumberjack20'] = self.lumberjack20
        self.stats_dict['mcghee'] = self.mcghee
        self.stats_dict['jack'] = self.jack
        self.stats_dict['bulger'] = self.bulger
        self.stats_dict['fight_gone_bad'] = self.fight_gone_bad

    def set_stat_value(self, stat_to_change, value):
        self.stats_dict[stat_to_change] = value

    def get_stat_value(self, stat_to_read):
        return self.stats_dict.get(stat_to_read)

    def presave_stats(self):
        self.snatch_1rm = self.stats_dict['snatch_1rm']
        self.power_snatch_1rm = self.stats_dict['power_snatch_1rm']
        self.hang_snatch_1rm = self.stats_dict['hang_snatch_1rm']
        self.squat_snatch_1rm = self.stats_dict['squat_snatch_1rm']

        self.clean_and_jerk_1rm = self.stats_dict['clean_and_jerk_1rm']

        self.hang_clean_1rm = self.stats_dict['hang_clean_1rm']
        self.power_clean_1rm = self.stats_dict['power_clean_1rm']
        self.squat_clean_1rm = self.stats_dict['squat_clean_1rm']

        self.split_jerk_1rm = self.stats_dict['split_jerk_1rm']
        self.push_jerk_1rm = self.stats_dict['push_jerk_1rm']
        self.push_press_1rm = self.stats_dict['push_press_1rm']
        self.shoulder_press_1rm = self.stats_dict['shoulder_press_1rm']

        self.backsquat_1rm = self.stats_dict['backsquat_1rm']
        self.backsquat_3rm = self.stats_dict['backsquat_3rm']
        self.backsquat_5rm = self.stats_dict['backsquat_5rm']

        self.front_squat_1rm = self.stats_dict['front_squat_1rm']
        self.front_squat_3rm = self.stats_dict['front_squat_3rm']
        self.front_squat_5rm = self.stats_dict['front_squat_5rm']

        self.deadlift_1rm = self.stats_dict['deadlift_1rm']
        self.deadlift_3rm = self.stats_dict['deadlift_3rm']
        self.deadlift_5rm = self.stats_dict['deadlift_5rm']

        self.angie = self.stats_dict['angie']
        self.barbara = self.stats_dict['barbara']
        self.chelsea = self.stats_dict['chelsea']
        self.cindy = self.stats_dict['cindy']
        self.diane = self.stats_dict['diane']
        self.elizabeth = self.stats_dict['elizabeth']
        self.fran = self.stats_dict['fran']
        self.grace = self.stats_dict['grace']
        self.nicole = self.stats_dict['nicole']
        self.helen = self.stats_dict['helen']
        self.isabel = self.stats_dict['isabel']
        self.jackie = self.stats_dict['jackie']
        self.karen = self.stats_dict['karen']
        self.mary = self.stats_dict['mary']
        self.nancy = self.stats_dict['nancy']
        self.annie = self.stats_dict['annie']
        self.eva = self.stats_dict['eva']
        self.kelly = self.stats_dict['kelly']
        self.jt = self.stats_dict['jt']
        self.michael = self.stats_dict['michael']
        self.murph = self.stats_dict['murph']
        self.daniel = self.stats_dict['daniel']
        self.josh = self.stats_dict['josh']
        self.filthy50 = self.stats_dict['filthy50']
        self.badger = self.stats_dict['badger']
        self.nate = self.stats_dict['nate']
        self.randy = self.stats_dict['randy']
        self.tommy_v = self.stats_dict['tommy_v']
        self.ryan = self.stats_dict['ryan']
        self.mr_joshua = self.stats_dict['mr_joshua']
        self.dt = self.stats_dict['dt']
        self.danny = self.stats_dict['danny']
        self.the_seven = self.stats_dict['the_seven']
        self.lumberjack20 = self.stats_dict['lumberjack20']
        self.mcghee = self.stats_dict['mcghee']
        self.jack = self.stats_dict['jack']
        self.bulger = self.stats_dict['bulger']
        self.fight_gone_bad = self.stats_dict['fight_gone_bad']

