from __future__ import unicode_literals
from django.db import models

class State(models.Model):
	state_id = models.CharField(max_length=200)
	state_name = models.CharField(max_length=200)
