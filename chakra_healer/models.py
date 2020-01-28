from django.db import models

# Create your models here.
class Chakras(models.Model):
    english_name = models.CharField(max_length=20)
    sanskrit_name = models.CharField(max_length=20)
    number = models.IntegerField()
    color = models.CharField(max_length=10)
    note = models.CharField(max_length=8)
    base_frequency = models.IntegerField()
    octave_half = models.IntegerField()
    octave_qtr = models.IntegerField()
    description	= models.TextField()
    sound = models.CharField(max_length=20)

    def __str__(self):
        return self.english_name

class UserData(models.Model):
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    home_chakra_number = models.IntegerField(null=True)
    home_note = models.CharField(max_length=2, null=True)
    home_frequency = models.IntegerField(null=True)

    def __str__(self):
        return self.user_name

class Conditions(models.Model):
    condition = models.CharField(max_length=30)
    primary_chakra = models.IntegerField()
    secondary_chakra = models.IntegerField(null=True)
    tertiary_chakra = models.IntegerField(null=True)
    
    def __str__(self):
        return self.condition