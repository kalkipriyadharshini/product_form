from djongo import models  

class Product(models.Model):
    productId = models.CharField(max_length=255, unique=True)  
    name = models.CharField(max_length=255)  
    description = models.TextField()  
    category = models.CharField(max_length=255)  
    price = models.FloatField()  
    stockQuantity = models.IntegerField()  
    ratings = models.FloatField(null=True, blank=True)  

    def __str__(self):
        return self.name
