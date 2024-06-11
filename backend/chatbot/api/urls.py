from django.urls import path
import os
print(os.path.dirname(os.path.realpath(__file__)))
from api.run_code import run
from api.Get_Serialized_table import upload_excel_file
urlpatterns = [
    path("api/run", run ),
    path("api/upload", upload_excel_file )
]