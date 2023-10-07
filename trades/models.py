from django.db import models

class Trade(models.Model):  
  user = models.ForeignKey( 
    'users.User', 
    related_name='trades', 
    on_delete=models.CASCADE, #If the owner is deleted, I want all their trades to be deleted too. 
    default=1
    # I AM NOT SURE IF I SHOULD MAKE THIS FIELD NON-REQUIRED. 
    # I AM MAKING IT REQUIRED FOR NOW BECAUSE I DO NO THINK I NEED THE DATABASE 
    # TO MAKE IT POSSIBLE FOR USERS TO GET THEIR ANALYSIS WITHOUT LOGGIN IN. 
    # BUT MAYBE THIS NEEDS TO BE CHANGED!
  ) 
  owner = models.TextField(blank=True, null=True)
  date = models.DateField() 
  ticker = models.CharField() 
  price = models.FloatField()
  shares = models.IntegerField() 
  costs = models.FloatField() 
  taxes = models.FloatField()
  currencyPair = models.CharField()
  comment = models.TextField(blank=True, null=True, max_length=250)