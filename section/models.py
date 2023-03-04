from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product',
        on_delete= models.CASCADE,
        null=True,
        related_name='+',
        blank=True
    )

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True)
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion,blank=True)

class Customer(models.Model):
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_CHOICE=[
        (MEMBERSHIP_GOLD,'gold'),
        (MEMBERSHIP_BRONZE,'bronze'),
        (MEMBERSHIP_SILVER,'silver')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True,blank=True)
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICE,default=MEMBERSHIP_BRONZE)