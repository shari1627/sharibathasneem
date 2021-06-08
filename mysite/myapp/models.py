from django.db import models
# # Create your models here.
# class Event(models.Model):
#     name = models.CharField(max_length=120,null=True)
#     phone= models.CharField(max_length=120,null=True)
#     email = models.CharField(max_length=60)
  
# class customer(models.Model):
#    name = models.CharField(max_length=120,null=True)
#    phone= models.CharField(max_length=120,null=True)
#    email = models.CharField(max_length=60)


#    def __str__(self): 
#       return self.name
      
      
class Customer(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    
    def register(self):
        self.save() 

    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        
    def get_customer_by_phone(Phone):
        try:
            return Customer.objects.get(Phone=Phone)
        except:
            return False
 
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False
    
    def isNumExists(self):
        if Customer.objects.filter(Phone=self.Phone):
            return True
        else:
            return False