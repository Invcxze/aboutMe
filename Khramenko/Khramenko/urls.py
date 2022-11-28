
from django.urls import path
from Vlad import views

urlpatterns = [
    path('', views.index, kwargs={'Name': "Vlad", "Surname": "Khramenko","interests": "Coding", "age":17  }),
    path('about', views.about, kwargs={'city':'Kazan', "school":"drummer, but I was an excellent student in robotics","study":"Yeah, i love it"}), 
    path('contact', views.contact, kwargs={'vk':"https://vk.com/slavakh","inst":"https://instagram.com/loon.cx", "github":"https://github.com/Invcxze"}),
]
