from django.db import models

# Create your models here.
class Location(models.Model):
	name = models.CharField(max_length = 120)
	city = models.CharField(max_length = 120)
	src_site = models.CharField(max_length = 120)
	locuOrFour_id = models.CharField(max_length = 120, null = True, blank = True)



	def __str__(self):
		return self.name


