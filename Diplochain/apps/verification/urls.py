from django.urls import path
from .views import (
    verifiview,

)

urlpatterns = [
    #path("<int:pk>", verifiview.as_view(), name="veri_fication"),
    path("<int:pk>", verifiview.as_view(), name="veri_fication"),
    path("create/", verifiview.as_view(), name="veri_fication"),

]
