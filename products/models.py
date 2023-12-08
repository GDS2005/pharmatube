from django.db import models

class Laboratory(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = 'labs' 

        def __str__(self):
            return self.id

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)
    address = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = 'suppliers' 

        def __str__(self):
            return self.id

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)
    address = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = 'clients' 

        def __str__(self):
            return self.id

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    dosage = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    expiration_date = models.DateField()
    height = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'  # Set the desired table name here. Else, the format will be {app_name}_{model_name}

    def __str__(self):
        return self.id

class Sell(models.Model):
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Sells:
            db_table = 'clients' 

    def __str__(self):
        return f"{self.client} bought {self.quantity} of {self.product}"

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'users' 

    def __str__(self):
        return self.id
    
class Rack(models.Model):
    category = models.IntegerField()

    class Meta:
        db_table = 'racks' 

    def __str__(self):
        return self.id

class Storing(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    x = models.DecimalField(max_digits=5, decimal_places=2)
    y = models.DecimalField(max_digits=5, decimal_places=2)
    z = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'storings' 

    def __str__(self):
        return self.id
