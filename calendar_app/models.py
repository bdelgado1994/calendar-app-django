from typing import Iterable
from django.db import models

class Event(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    initial_date=models.DateTimeField()
    final_date=models.DateTimeField()
    
    def __str__(self) -> str:
        return str(self.title)
    
    def save(self, *args,**kwargs) -> None:
        self.title=self.title.capitalize()
        return super(Event,self).save(*args,**kwargs)
    class Meta:
        db_table="event"
