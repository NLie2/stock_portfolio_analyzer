from django.db import models

class Trade(models.Model):  
  tradeTable = models.ForeignKey(
    'tradetables.Tradetable', 
    related_name = 'trades', 
    on_delete= models.CASCADE, #If the owner is deleted, I want all their trade tables to be deleted too. 
  )
  date = models.DateField() 
  ticker = models.CharField() 
  price = models.FloatField()
  shares = models.IntegerField() 
  costs = models.FloatField() 
  taxes = models.FloatField()
  currencyPair = models.CharField()