import django_filters
from .models import *


class GearFilter(django_filters.FilterSet):
	class Meta:
		model = Gear
		fields = '__all__'
