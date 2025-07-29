from django.db import models

# Create your models here.
class Crud(models.Model):
    title=models.CharField(max_length=50,null=True,blank=True)
    price=models.DecimalField(max_digits=5 , decimal_places=2)
    taxes=models.DecimalField(max_digits=5 , decimal_places=2)
    ads=models.DecimalField(max_digits=5 , decimal_places=2)
    discount=models.DecimalField(max_digits=5 , decimal_places=2)
    category=models.CharField(max_length=50,null=True,blank=True)
    
    @property
    def total(self):
        return (self.price + self.taxes + self.ads) - self.discount