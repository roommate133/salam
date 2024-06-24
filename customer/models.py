from django.db import models
from django.contrib.auth.models import User
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    created=models.DateField(auto_now_add=True)
    
    def __str__(self) :
        return f"{self.name} - {self.created}"
    

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.get_full_name()