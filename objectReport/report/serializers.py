from rest_framework_mongoengine.serializers import DocumentSerializer
from rest_framework.renderers import JSONRenderer
from report.models import Report

class ReportSerializer(DocumentSerializer):
    class Meta:
        model = Report
        fields = '__all__'
