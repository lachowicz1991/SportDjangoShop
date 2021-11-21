from django.db import models
from django.db.models import CharField, Model, ManyToManyField, SlugField, DO_NOTHING, DateField, DateTimeField, ForeignKey, FloatField, IntegerField, TextField
from django.utils.text import slugify
# Create your models here.


class SportBranch(Model):
	sport_branch = CharField(max_length=128)

	def __str__(self):
		return self.sport_branch


class Outfit(Model):
	GENDER_ARRAY = (('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex'))
	SIZE_ARRAY = (('XL', 'XL'), ('L', 'L'), ('M', 'M'), ('S', 'S'))
	AVAILABLE = (('Yes', 'Yes'), ('No', 'No'))

	outfit_name = CharField(max_length=128,)
	size = CharField(max_length=128, null=True, choices=SIZE_ARRAY)
	gender = CharField(max_length=128, null=True, choices=GENDER_ARRAY)
	sport_branch = ManyToManyField(SportBranch)
	description = TextField(max_length=200, null=True)
	price = FloatField(null=True)
	availability = CharField(max_length=128, null=True, choices=AVAILABLE)

	def __str__(self):
		return self.outfit_name


class Gear(Model):
	RENTAL = (('For Rent', 'For Rent'), ('Not For Rent', 'Not For Rent'))
	AVAILABLE = (('Yes', 'Yes'), ('No', 'No'))

	gear_name = CharField(max_length=128, null=True)
	sport_branch = ManyToManyField(SportBranch)
	availability = CharField(max_length=128, null=True, choices=AVAILABLE)
	description = TextField(max_length=200, null=True)
	rent = CharField(max_length=128, null=True, choices=RENTAL)
	rent_price = FloatField(null=True)
	price = FloatField(null=True)

	def __str__(self):
		return self.gear_name