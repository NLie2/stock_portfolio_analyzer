from django.db import models

class Tradetable(models.Model):
  user = models.ForeignKey( 
    'users.User', 
    related_name='tradetables', 
    on_delete=models.CASCADE, #If the owner is deleted, I want all their tradetables to be deleted too. 
    default=1
  ) 
  owner = models.TextField(blank=True, null=True)