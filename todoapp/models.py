from django.db import models

class TodoItem(models.Model):
    todo = models.CharField(max_length=200)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.todo 
    

