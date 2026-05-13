from django.urls import path

from .views import GenerateDocumentsView
from .views import MyDocumentsListView


urlpatterns = [
    path("generate/", GenerateDocumentsView.as_view(), name="generate_documents"),
    path("my/", MyDocumentsListView.as_view(), name="my_documents"),
]