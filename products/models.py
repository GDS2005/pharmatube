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
    height = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    length = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'products'  # Set the desired table name here. Else, the format will be {app_name}_{model_name}

    def __str__(self):
        return self.product_name
