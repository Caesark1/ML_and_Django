from django.shortcuts import render
from django.http import JsonResponse
from .utils import main
from django.views.generic.base import TemplateView
from .models import Passenger
import numpy as np 
import pandas as pd
import seaborn as sns



class IndexListView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        content = main()
        context["datasets"] = content
        return context


def get_json_obj(request):
    json_inter = pd.read_csv("model/titanic.csv")
    convert = json_inter.to_json()
    context = {"json": convert}
    return render(request, "json.html", context)


# Пытался сделать через БД. Не смог т.к. у некоторых не было поля Age вообще, и выдавало ошибку по типу "Age column is not defined"

# def index(request):
#     qs = Passenger.objects.all()
#     titanic_df = pd.DataFrame(qs)
#     is_18 = titanic_df["Age"] >= 18 # if include 18 use this
#     # is_18 = titanic_df["Age"] > 18 # if not include 18 use this
#     more_than_18 = titanic_df[is_18].sort_values("Age")
#     first_10 = more_than_18.head(10)
#     context = first_10
#     return render(request, "index.html", {})