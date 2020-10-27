from rest_framework import viewsets

from .models import Printer, Check
from .serializers import PrinterSerializer, CheckSerializer


class PrinterModelViewSet(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


class CheckModelViewSet(viewsets.ModelViewSet):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer



