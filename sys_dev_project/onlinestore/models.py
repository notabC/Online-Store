from django.db import models


# Create your models here.
class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_no = models.IntegerField()
    item_description = models.CharField(max_length=1000)
    item_price = models.DecimalField(max_digits=11, decimal_places=2)
    # number_of_items = models.IntegerField()

   