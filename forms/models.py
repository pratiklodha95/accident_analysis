from __future__ import unicode_literals
from django.db import models

class State(models.Model):
	state_id = models.CharField(max_length=200)
	state_name = models.CharField(max_length=200)

class Districts(models.Model):
	state = models.ForeignKey(State)
	district_id = models.CharField(max_length=200)
	district_name = models.CharField(max_length=200)

class AccidentDate(models.Model):
	district = models.ForeignKey(Districts)
	firno = models.CharField(max_length=200)
	policestation = models.CharField(max_length=200)
	accidentdate = models.DateField()

	# all the other fields in the form have to be included here