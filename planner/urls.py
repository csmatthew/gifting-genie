from django.urls import path
from . import views

app_name = 'planner'

urlpatterns = [
    path('<int:user_id>/calendar/', views.calendar_view, name='calendar_view'),
    path('<int:user_id>/calendar/add/', views.add_event, name='add_event'),
    path('<int:user_id>/calendar/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('<int:user_id>/calendar/delete/<int:event_id>/', views.delete_event, name='delete_event'),
]