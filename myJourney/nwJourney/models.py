from django.db import models

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    interests = models.TextField()
    goals = models.TextField()

    def __str__(self):
        return self.name

class LearningJourney(models.Model):
    week = models.IntegerField()
    topic = models.CharField(max_length=200)
    key_learning = models.TextField()

    def __str__(self):
        return f"Week {self.week} - {self.topic}"
