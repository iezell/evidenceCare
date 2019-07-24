from django.urls import include, path

urlpatterns = [
    path(r'report/', include('report.urls')),
]
