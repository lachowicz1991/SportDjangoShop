from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [

	path('', HomeView.as_view(), name='index'),
	path('employee', EmployeeView.as_view(), name='employee'),
	path('sort', gear_sort, name='home'),
	path('gear', GearListView.as_view(), name='gear'),
	path('gear_detail/<int:pk>', GearDetailView.as_view(), name='gear_detail'),
	path('gear/add', GearCreateView.as_view(), name='gear-create'),
	path('gear/<int:pk>/remove', GearDeleteView.as_view(), name='gear-delete'),
	path('gear/<int:pk>/update', GearUpdateView.as_view(), name='gear-update'),
	path('outfit', OutfitListView.as_view(), name='outfit'),
	path('outfit_detail/<int:pk>', OutfitDetailView.as_view(), name='outfit_detail'),
	path('sort2', outfit_sort, name='home'),
	path('outfit/add', OutfitCreateView.as_view(), name='outfit-create'),
	path('outfit/<int:pk>/remove', OutfitDeleteView.as_view(), name='outfit-delete'),
	path('outfit/<int:pk>/update', OutfitUpdateView.as_view(), name='outfit-update'),
	# path('products/', Products.as_view(), name='product'),
]