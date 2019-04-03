from django.db import models

class Click(models.Model):

    name = models.CharField(max_length=50)
    click_count = models.IntegerField()

    def __str__(self):
        return self.name

