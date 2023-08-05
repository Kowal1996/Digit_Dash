from django.db import models
from accounts.models import Profile
# Create your models here.
class OneOutOfTwenty(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE),
    score = models.PositiveBigIntegerField(default=0),
    gameDate = models.DateTimeField(auto_now_add=True),
    luckyNumber = models.IntegerField()
