from django.db import models
from django.contrib.auth import get_user_model

class Plant(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    scientific_name = models.CharField(max_length=100, blank=True)
    flower_color = models.CharField(max_length=64, blank=True)
    description = models.TextField(blank=True)
    bloom_time = models.CharField(max_length=64, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

