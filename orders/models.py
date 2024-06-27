from django.db import models
from.utils import format_phone_number
from django.contrib.auth.models import AbstractUser

# 2e473895d081015a2377878756fb4bca
# Create your models here.

class Customer(AbstractUser):
  name = models.CharField(max_length=255)
  username =  models.CharField(max_length=255,unique=True)
  customer_code = models.CharField(max_length=100, unique=True)
  phone_number = models.CharField(max_length=15, default="0700298415")

  def save(self, *args, **kwargs):
      self.phone_number = format_phone_number(self.phone_number)
      super().save(*args, **kwargs)

  def __str__(self) -> str:
      return self.name
# class Customer(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers', null=True)
#   name = models.CharField(max_length=255)
#   code = models.CharField(max_length=100, unique=True)
#   phone_number = models.CharField(max_length=15,null=True)



  # def __str__(self) -> str:
  #   return self.name

  # def save(self, *args, **kwargs):
  #   self.phone_number = format_phone_number(self.phone_number)
  #   super().save(*args, **kwargs)



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.item} - {self.amount}"

