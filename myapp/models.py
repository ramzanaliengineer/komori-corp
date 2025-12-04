from django.db import models
# makemigrations- create changes and store in a file
# migrate - apply the pending changes created by makemigrations
# Create your models here.
class Contact(models.Model):
    name= models.CharField( max_length=50)
    email= models.CharField(max_length=100)
    phone= models.CharField(max_length=12)
    desc= models.TextField()
    date= models.DateField()


    def __str__(self):
        return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='products/')
#     price = models.IntegerField()

# class RelevantImages(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='relevant/')


# from django.db import models

# class Product(models.Model):
#     title = models.CharField(max_length=200)
#     price = models.IntegerField()
#     main_image = models.ImageField(upload_to="products/")
#     related_image = models.ImageField(upload_to="products/")

#     def __str__(self):
#         return self.title

