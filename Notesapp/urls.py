from django.urls import path

from Notesapp import views

app_name = 'Notesapp'

urlpatterns = [

    path('', views.notes_list.as_view(), name="note_list"),

]