from django.urls import path
import os
print(os.path.dirname(os.path.realpath(__file__)))
from api.run_code import run

urlpatterns = [
    path("api/", run )
]