from django.db import models
from django.forms import ModelForm
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    product_type = models.CharField(max_length=100)
    def __str__(self):
        return self.product_type

class NewItem(models.Model):
    TSHIRT_SIZES = (
    ("xs","Xsmall"),
    ("s","Small"),
    ("m","Medium"),
    ("l","Large"),
    ("xl","Xlarge"),
    ("xxl","XXLarge"),)

    COLOR_CHOICE = (
    ("blue","Blue"),
    ("green","Green"),
    ("black","Black"),
    ("yellow","Yellow"),
    ("grey","Grey"),
    ("white","White"),
    ("royal blue","Royal Blue"),
    ("orange","Orange"),
    ("pink","Pink"),
    ("navy","Navy"),
    ("purple","Purple"),
    ("red","Red"),
    ("lime","Lime"),
    ("grey melange","Grey Melange"),
    ("stone","Stone"),
    ("sky blue","Sky Blue"),
    ("maroon","Maroon"),
    ("emerald green","Emerald Green"),
    ("teal","Teal"),
    ("grey","Grey"),
    ("dark green","Dark Green"),
    ("army green","Army Green"),
    ("grass green","Grass Black"),
    ("turqouise","Turqouise"),
    ("Cerise","Cerise"),)

    ITEM_CHOICE = (
    ("Tshirt145G","Tshirt145G"),
    ("Tshirt165G","Tshirt165G"),
    ("Tshirt180G","Tshirt180G"),
    ("LS.Tshirt145G","LS.Tshirt145G"),
    ("LS.Tshirt165G","LS.Tshirt165G"),
    ("LS.Tshirt180","LS.Tshirt180G"),
    ("Golfer145G","Golfer145G"),
    ("Golfer165G","Golfer165G"),
    ("Golfer180G","Golfer180G"),
    ("LS.Golfer145G","LS.Golfer145G"),
    ("LS.Golfer165G","LS.Golfer165G"),
    ("LS.Golfer180G","LS.Golfer180G"),
    ("Hoody","Hoody"),
    ("Cap","Cap"),
    ("Beanie","Beanie"))

    model = Product
    product_type = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.CharField(max_length=20,choices=ITEM_CHOICE)
    size = models.CharField(max_length=20,choices=TSHIRT_SIZES)
    color = models.CharField(max_length=20,choices=COLOR_CHOICE)
    amount = models.IntegerField(default=0)



    def __str__(self):
        return self.description
