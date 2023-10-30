from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    dosage = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    expiration_date = models.DateField()
    supplier_id = models.IntegerField()
    supplier_name = models.CharField(max_length=100)
    supplier_contact = models.CharField(max_length=100)
    date_received = models.DateField()

    def __str__(self):
        return self.product_name
