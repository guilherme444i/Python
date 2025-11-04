from django.db import models

class tasK(models.model):
    label = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def _str_(self):
        return self.label
    
    
