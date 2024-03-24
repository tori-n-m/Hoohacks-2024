from django.db import models

# Create your models here.
'''
class Choices(models.Model):
    description = models.CharField(max_length=300)

class Profile(models.Model):
   user = models.ForeignKey(User, blank=True, unique=True, verbose_name_='user')
   the_choices = models.ManyToManyField(Choices)

'''

'''
class Subject(models.Model):
	name = models.CharField(max_length=100)
	grade = models.IntegerField(max_length=30)
	completion = models.CharField(default=30)  
	
class English(models.Subject):
    name = models.CharField('English')
    grade = models.CharField('A')
    completion = models.CharField('85%')

class Math(models.Subject):
    name = models.CharField('Math')
    grade = models.CharField('C')
    completion = models.CharField('60%')

class Science(models.Subject):
    name = models.CharField('Science')
    grade = models.CharField('A')
    completion = models.CharField('90%')

class History(models.Subject):
    name = models.CharField('History')
    grade = models.CharField('B')
    completion = models.CharField('82%')

    '''

 
def __str__(self):
	return (self.first_name + " " + self.last_name)