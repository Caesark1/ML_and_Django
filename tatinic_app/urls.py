from django.urls import path
from . import views


urlpatterns = [
    path('',views.IndexListView.as_view(), name = "index"),
    path('data.json/', views.get_json_obj, name = "json")
]