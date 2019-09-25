from django.urls import path
from .views import homePageView, ContactView, questions

urlpatterns = [
	path('', homePageView, name='home'),
	path('contact/', ContactView.as_view(), name='contact'),
	path('contact/mensajes', questions, name='mensajes'),
]