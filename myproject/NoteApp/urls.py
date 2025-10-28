from django.urls import path
from .import views

urlpatterns = [
    path("", views.get_all_notes,name="all_notes"),
    path("Create/", views.create_notes,name="Note_create"),
    path("update/<int:pk>/", views.update_notes,name="update_note"),
    path("delete/<int:pk>/", views.delete_note,name="delete_note"),
]
