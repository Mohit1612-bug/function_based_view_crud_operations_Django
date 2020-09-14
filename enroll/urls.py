from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="homepage"),
    path('update/<int:id>/',views.update,name="updatedata"),
    path('delete/<int:id>/',views.delete_data,name="deletedata"),
]
