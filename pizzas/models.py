from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length = 50)
    picture = models.ImageField(upload_to = 'img', null = True, blank = True)

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    topping_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.topping_name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.text[:50]}...'