from django.urls import path
from django.contrib.auth.views import LoginView
from .views import HomeView, gear_sort, EmployeeView, GearDeleteView, GearUpdateView, GearCreateView, GearListView, OutfitListView, GearDetailView

urlpatterns = [

	path('', HomeView.as_view(), name='index'),
	path('employee', EmployeeView.as_view(), name='employee'),
	path('sort', gear_sort, name='home'),
	path('gear', GearListView.as_view(), name='gear'),
	path('gear_detail/<int:pk>', GearDetailView.as_view(), name='gear_detail'),
	path('gear/add', GearCreateView.as_view(), name='gear-create'),
	path('gear/<int:pk>/remove', GearDeleteView.as_view(), name='gear-delete'),
	path('gear/<int:pk>/update', GearUpdateView.as_view(), name='gear-update'),
	# path('products/', Products.as_view(), name='product'),
]