from django.db import models

# Create your models here.
class Chakras(model.Model):
    english_name = models.CharField(max_length=20)
    sanskrit_name = models.CharField(max_length=20)
    number = models.U=IntegerField()
    color = models.CharField(max_length=10)
    note = models.CharField(max_length=2)
    base_frequency = models.IntegerField
    octave_one = models.IntegerField()
    octave_two = models.IntegerField()
    description	= models.TextField()
    sound = models.CharField(max_length=20)

    def __str__(self):
        return self.english_name

class UserData(model.Model):
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    home_chakra_number = models.IntegerField()
    home_note = models.CharField(max_length=2)
    home_frequency = models.IntegerField()

    def __str__(self):
        return self.user_name

class Conditions(model.Model):
    condition = models.CharField(max_length=20)
    primary_chakra = models.IntegerField()
    secondary_chakra = models.IntegerField(nulls=True)
    tertiary_chakra = models.IntegerField(nulls=True)
    
    def __str__(self):
        return self.condition