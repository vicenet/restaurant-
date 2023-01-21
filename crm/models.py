from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone=models.IntegerField(null=True)
    email=models.EmailField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class tag(models.Model):
    name=models.CharField(max_length=200,null=True)
    

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
          ('Dessert','Dessert'),('Meal','Meal'),('Beverage','Beverage')
    )


    name=models.CharField(max_length=200,null=True)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    description=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tags=models.ManyToManyField(tag)

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS=(('Pending', 'Pending'),
            ('Served', 'Served'),
            ('Unpaid', 'Unpaid'),
            ('Paid','Paid')
            ,)
    cutomer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        return self.product.name
    
