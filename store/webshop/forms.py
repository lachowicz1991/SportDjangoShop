from django.forms import CharField, DateField, Form, FloatField, IntegerField, ModelChoiceField, ModelForm, Textarea
from django.core.exceptions import ValidationError
from .models import *
import re

def capitalized_validator(value):
	if value[0].islower():
		raise ValidationError('First letter must be capital!')

class OutfitForm(ModelForm):
	class Meta:
		model = Outfit
		fields = '__all__'
		exclude = ['slug']
	GENDER_ARRAY = (('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex'))
	SIZE_ARRAY = (('XL', 'XL'), ('L', 'L'), ('M', 'M'), ('S', 'S'))
	AVAILABLE = (('Yes', 'Yes'), ('No', 'No'))

	outfit_name = CharField(max_length=128, validators=[capitalized_validator])
	size = CharField(max_length=128, null=True, choices=SIZE_ARRAY)
	gender = CharField(max_length=128, null=True, choices=GENDER_ARRAY)
	sport_branch = ManyToManyField(SportBranch)
	availability = CharField(max_length=128, null=True, choices=AVAILABLE)
	description = TextField(max_length=200, null=True)
	price = FloatField(null=True)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

class GearForm(ModelForm):
	class Meta:
		model = Gear
		fields = '__all__'
		exclude = ['slug']

	RENTAL = (('For Rent', 'For Rent'), ('Not For Rent', 'Not For Rent'))
	AVAILABLE = (('Yes', 'Yes'), ('No', 'No'))

	gear_name = CharField(max_length=128, validators=[capitalized_validator])
	sport_branch = ManyToManyField(SportBranch)
	availability = CharField(max_length=128, null=True, choices=AVAILABLE)
	description = TextField(max_length=200, null=True)
	rent = CharField(max_length=128, null=True, choices=RENTAL)
	rent_price = FloatField(null=True)
	price = FloatField(null=True)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	# def clean_description(self):
	# 	initial = self.cleaned_data['description']
	# 	sentences = re.sub(r'\s*\.\s*','.',initial).split('.')
	# 	return '.'.join(sentence.capitalize() for sentence in sentences)