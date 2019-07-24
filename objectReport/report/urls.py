from django.urls import include, path
from report import views

urlpatterns = [
    path(r'', views.ReportView.as_view(), name='polls'),
]
