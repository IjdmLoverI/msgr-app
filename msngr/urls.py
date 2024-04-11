from django.urls import path

from msngr.views import (
    index,

)

urlpatterns = [
    path("", index, name="index")
]

app_name = "msngr"
