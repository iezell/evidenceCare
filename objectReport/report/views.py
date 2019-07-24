from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from report.models import Report
from report.serializers import ReportSerializer

import datetime

class ReportView(APIView):

    def post(self, request, format=None):
        data = request.data
        serializer = ReportSerializer(data=data)
        if serializer.is_valid():
            classDict = serializer.validated_data['classObject']

            try:
                oldReport = Report.objects.filter(pid=serializer.validated_data['pid'],
                                                  classId=serializer.validated_data['classId'])
            except Report.DoesNotExist:
                pass

            if 'objectAttr' in classDict:
                if oldReport:
                    classDict.update({'operation':'updated'})
                else:
                    classDict.update({'operation':'created'})

                changed = [key for key, value in classDict['objectAttr'].items() if value is not ""]
                data = {key:value for key, value in classDict['objectAttr'].items() if value is not ""}
                del classDict['objectAttr']

            else:
                changed = 'null'
                data = 'null'

            classDict.update({'changed':changed})
            classDict.update({'data':data})
            classDict.update({'time':datetime.datetime.now().isoformat()})
            classDict.update({'pk':1})
            serializer.save(classObject=classDict)

            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)
