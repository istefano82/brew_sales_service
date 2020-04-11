from django.db import models

class SalesItem(models.Model):
    title = models.CharField(max_length=200)
    sales_amount = models.IntegerField()
    sales_person = models.CharField(max_length=200)


    def __str__(self):
        return self.title