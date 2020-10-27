from django.db import models

CHECK_TYPES = [
    ('KITCHEN', 'kitchen'),
    ('CLIENT', 'client'),
]


class Printer(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255, unique=True)
    check_type = models.CharField(max_length=255, choices=CHECK_TYPES)
    point_id = models.IntegerField()


class Check(models.Model):
    STATUSES = (
        ('NEW', 'new'),
        ('RENDERED', 'rendered'),
        ('PRINTED', 'printed'),
    )
    printer_id = models.ForeignKey(Printer, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=CHECK_TYPES)
    order = models.JSONField(default={})
    status = models.CharField(max_length=255, choices=STATUSES)
    pdf_file = models.FileField(upload_to='file/')
