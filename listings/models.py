from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    image6 = models.ImageField(null=True, blank=True)
    image7 = models.ImageField(null=True, blank=True)
    image8 = models.ImageField(null=True, blank=True)
    image9 = models.ImageField(null=True, blank=True)
    image10 = models.ImageField(null=True, blank=True)
    image11 = models.ImageField(null=True, blank=True)
    image12 = models.ImageField(null=True, blank=True)
    image13 = models.ImageField(null=True, blank=True)
    image14 = models.ImageField(null=True, blank=True)
    image15 = models.ImageField(null=True, blank=True)
    image16 = models.ImageField(null=True, blank=True)
    image17 = models.ImageField(null=True, blank=True)
    image18 = models.ImageField(null=True, blank=True)
    image19 = models.ImageField(null=True, blank=True)
    image20 = models.ImageField(null=True, blank=True)
    image21 = models.ImageField(null=True, blank=True)
    image22 = models.ImageField(null=True, blank=True)
    image23 = models.ImageField(null=True, blank=True)
    image24 = models.ImageField(null=True, blank=True)
    image25 = models.ImageField(null=True, blank=True)
    image26 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
